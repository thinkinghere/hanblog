from sanic import Blueprint

from ext import mako
from models import Post

bp = Blueprint('views')


@bp.route('/')
@mako.template('index.html')
async def index(request):
    # print(request.args)
    # name = request.args.get('title', 'World')
    name = "world"
    post = await Post.create(title=name)
    print(await Post.filter(title=name).first())
    return {'post': post}
