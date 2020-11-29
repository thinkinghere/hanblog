from tortoise import fields

from .base import BaseModel


class Comment(BaseModel):
    github_id = fields.IntField()
    post_id = fields.IntField()
    reaction_type = fields.IntField()
    ref_id = fields.IntField(default=0)

    class Meta:
        table = 'comments'
