from tortoise.models import Model
from tortoise import fields
from sanic.exceptions import abort
from .mc import cache, clear_mc

MC_KEY_ITEM_BY_ID = '%s:%s'


class BaseModel(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    @classmethod
    @cache(MC_KEY_ITEM_BY_ID  % ('{cls.__name__}', '{id}'))
    async def cache(cls, id):
        return await cls.filter(id=id).first()

    @classmethod
    async def get_or_404(cls, id, sync=False):
        obj = await cls.cache(id)
        if not obj:
            abort(404)
        if sync:
            return await obj.to_sync_dict()
        return obj

