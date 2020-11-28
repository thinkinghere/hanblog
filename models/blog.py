from tortoise import fields

from .base import BaseModel


class Post(BaseModel):
    title = fields.TextField()

    class Meta:
        table = 'posts'


class Tag(BaseModel):
    name = fields.TextField()

    class Meta:
        table = 'tags'


class PostTag(BaseModel):
    post_id = fields.IntField()
    tag_id = fields.IntField()

    class Meta:
        table = 'post_tags'
