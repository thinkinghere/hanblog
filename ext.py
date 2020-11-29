from tortoise import Tortoise
from sanic_mako import SanicMako

from config import DB_URL

mako = SanicMako()


async def init_db(create_db=False):
    await Tortoise.init(
        db_url=DB_URL,
        modules={'models': ['models']},
        _create_db=create_db
    )
