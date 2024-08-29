from pydantic import UUID4, BaseModel, field_serializer


class PolicyCategorySchema(BaseModel):
    id: UUID4
    name: str
    server_id: UUID4
    policies: list["PolicySchema"]


class PolicySchema(BaseModel):
    id: UUID4
    name: str
    value: int | bool | str

    @field_serializer("value")
    def serialize_value(self, value: int | bool | str):
        try:
            return bool(value) if value in ("true", "false") else int(value)
        except ValueError:
            return value


class OwnerSchema(BaseModel):
    pass
