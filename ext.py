from tortoise import Tortoise

from config import DB_URL


async def init(create_db):
    await Tortoise.init(
        db_url=DB_URL,
        modules={'models': ['models.base', 'models.blog', 'models.comments', 'models.react']},
        _create_db=create_db
    )


