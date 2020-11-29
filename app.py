from sanic import Sanic

from ext import mako, init_db
from config import DEBUG

from views import bp

app = Sanic(__name__)
mako.init_app(app)
app.blueprint(bp)
app.static('/static', './static')


@app.listener('before_server_start')
async def setup_db(app, loop):
    await init_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=DEBUG)
