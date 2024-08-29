from typing import Annotated

from fastapi import APIRouter, Path, Response, Depends, Body
from pydantic import UUID4
from tortoise.transactions import in_transaction

from ..dependencies import Pagination
from ..exceptions import UserExistsError, UserDoesNotExistError
from ..models import Users, Creds
from ..schemas import UserRegister, UserOut, UserIn
from ..utils.security import get_password_hash

router = APIRouter(prefix='/users')


@router.post('/', response_model=UserOut)
async def register_user(response: Response, creds: UserRegister):
    async with in_transaction() as conn:
        if user_id_db := await Creds.get_or_none(login=creds.login, using_db=conn):
            raise UserExistsError(user_id_db.user_id)
        user = await Users.create(using_db=conn)
        await Creds.create(user=user, login=creds.login, passwd=get_password_hash(creds.passwd))
    response.status_code = 201
    return user


@router.get('/all')
async def get_all_users(pagination: Annotated[Pagination, Depends()]):
    async with in_transaction() as conn:
        all_users = Users.all(using_db=conn)
        filtered = await all_users.offset(pagination.start).limit(pagination.limit)
        count = await all_users.count()
        return {
            'users': filtered,
            'count': count
        }


@router.get('/{user_id}')
async def get_user(user_id: Annotated[UUID4, Path()]):
    async with in_transaction() as conn:
        if user_in_db := await Users.get_or_none(id=user_id, using_db=conn):
            return user_in_db
        raise UserDoesNotExistError(user_id)


@router.delete('/{user_id}')
async def get_user(response: Response, user_id: Annotated[UUID4, Path()]):
    async with in_transaction() as conn:
        if user_in_db := await Users.get_or_none(id=user_id, using_db=conn):
            await user_in_db.delete(using_db=conn)
            response.status_code = 204
            return {'status': 'deleted'}
        raise UserDoesNotExistError(user_id)


@router.put('/{user_id}', response_model=UserOut)
async def edit_user(response: Response, user_id: Annotated[UUID4, Path()], edit_data: Annotated[UserIn, Body()]):
    async with in_transaction() as conn:
        if user_in_db := await Users.get_or_none(id=user_id, using_db=conn):
            await user_in_db.update_from_dict(edit_data.model_dump())
            await user_in_db.save(using_db=conn)
            response.status_code = 202
            return await user_in_db.get(id=user_id, using_db=conn)
        raise UserDoesNotExistError(user_id)
