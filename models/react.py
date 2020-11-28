from tortoise import fields

from .base import BaseModel


class ReactItem(BaseModel):
    post_id = fields.IntField()
    reaction_type = fields.IntField()

    class Meta:
        table = 'react_items'
