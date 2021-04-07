from tortoise import Tortoise
from sanic_mako import SanicMako
from sanic_auth import Auth
from config import DB_URL

mako = SanicMako()
auth = Auth()


async def init_db(create_db=False):
    await Tortoise.init(
        db_url=DB_URL,
        modules={'models': ['models']},
        _create_db=create_db
    )
