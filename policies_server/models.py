from tortoise import Model, fields
from tortoise.contrib.postgres.fields import ArrayField


class PolicyCategoryModel(Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=255)
    server_id = fields.UUIDField(null=False)

    policies: fields.ReverseRelation["PolicyModel"]

    async def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'server_id': self.server_id
        }


class PolicyModel(Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=255)
    allowed_values = ArrayField(element_type="text")

    category: fields.ForeignKeyRelation[PolicyCategoryModel] = fields.ForeignKeyField('main.PolicyCategoryModel',
                                                                                      'policies')

    async def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            "allowed_values": self.allowed_values
        }
