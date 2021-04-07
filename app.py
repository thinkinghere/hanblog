import aiohttp
import asyncio
import aiomcache
from sanic import Sanic
from sanic_session import Session, MemcacheSessionInterface
from ext import mako, init_db
from config import DEBUG

from views.admin import bp as admin_bp
from views.index import bp as index_bp


import config
from ext import mako, init_db, auth
from pathlib import Path

app = Sanic(__name__)
app.config.from_object(config)
auth.setup(app)
mako.init_app(app)
app.blueprint(admin_bp)
app.blueprint(index_bp)
app.static('/static', './static')

session = Session()


@app.listener('before_server_start')
async def setup_db(app, loop):
    await init_db()
    client = aiomcache.Client(config.MEMCACHED_HOST, config.MEMCACHED_PORT, loop=loop)  # noqa
    session.init_app(app, interface=MemcacheSessionInterface(client))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=DEBUG)
