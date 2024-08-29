from pathlib import Path as OSPath
from typing import Annotated

from aiofiles import open as aiopen
from fastapi import FastAPI, Path, Body, Security
from fastapi.responses import ORJSONResponse
from pydantic import UUID4
from tortoise.contrib.fastapi import register_tortoise
from tortoise.transactions import in_transaction

from .models import PolicyModel, PolicyCategoryModel
from .schemas import PolicySchema, OwnerSchema
from .settings import TORTOISE_ORM

app = FastAPI()
register_tortoise(app, TORTOISE_ORM, generate_schemas=True)
policies_path = OSPath(__file__).parent / 'policies'


async def get_resourse_owner():
    pass


@app.get('/all_policies')
async def get_all_policies(owner: Annotated[OwnerSchema, Security(get_resourse_owner, scopes=["policies.all.get"])]):
    async with in_transaction() as conn:
        policies_categories = await PolicyCategoryModel.all(using_db=conn).prefetch_related('policies')
        servers = {k.server_id: [] for k in policies_categories}
        for policies_category in policies_categories:
            category = await policies_category.to_dict()
            policies = []
            for policy in policies_category.policies:
                dict_policy = await policy.to_dict()
                async with aiopen(policies_path / str(policy.id)) as f:
                    dict_policy['value'] = await f.read()
                policies.append(PolicySchema(**dict_policy))
            category['policies'] = policies
            category.pop('server_id')
            servers[policies_category.server_id].append(category)
        return {'servers': servers}


@app.get('/{server_id}/all_policies')
async def get_all_server_policies(server_id: Annotated[UUID4, Path()],
                                  owner: Annotated[OwnerSchema, Security(get_resourse_owner, scopes=["policies.own.get"])]):
    async with in_transaction() as conn:
        policies_categories = await PolicyCategoryModel.filter(server_id=server_id).using_db(conn).prefetch_related(
                'policies')

        categories = []
        for policies_category in policies_categories:
            category = await policies_category.to_dict()
            policies = []
            for policy in policies_category.policies:
                dict_policy = await policy.to_dict()
                async with aiopen(policies_path / str(policy.id)) as f:
                    dict_policy['value'] = await f.read()
                policies.append(PolicySchema(**dict_policy))
            category['policies'] = policies
            category.pop('server_id')
            categories.append(category)
        return {'servers': {server_id: categories}}


@app.get('/{server_id}/{policy_id}')
async def get_policy_for_server(server_id: Annotated[UUID4, Path()],
                                policy_id: Annotated[UUID4, Path()],
                                owner: Annotated[OwnerSchema, Security(get_resourse_owner, scopes=["policies.own.get"])]):
    async with in_transaction() as conn:
        if policy := await PolicyModel.get_or_none(id=policy_id, category__server_id=server_id, using_db=conn):
            async with aiopen(policies_path / str(policy.id)) as f:
                return {'value': await f.read()}
    return ORJSONResponse(status_code=400, content={'error': 'policy_not_exist',
                                                    'description': 'Requested policy does not exist'})


@app.patch('/{policy_id}')
async def edit_policy(policy_id: Annotated[UUID4, Path()],
                      new_value: Annotated[str, Body(embed=True)],
                      owner: Annotated[OwnerSchema, Security(get_resourse_owner, scopes=["policies.set"])]):
    async with in_transaction() as conn:
        if policy := await PolicyModel.get_or_none(id=policy_id, using_db=conn):
            if new_value in policy.allowed_values:
                async with aiopen(policies_path / str(policy.id), mode='w') as f_w:
                    await f_w.write(new_value)
                async with aiopen(policies_path / str(policy.id)) as f_r:
                    return {'value': await f_r.read()}
            return ORJSONResponse(status_code=400, content={'error': 'value_not_allowed',
                                                            'description': f'Invalid value. Possible values are: {policy.allowed_values}'})
        return ORJSONResponse(status_code=400, content={'error': 'policy_not_exist',
                                                        'description': 'Requested policy does not exist'})
