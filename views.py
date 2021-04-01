from sanic import Blueprint

from ext import mako
from models import Post

bp = Blueprint('views')


@bp.route('/')
@mako.template('index.html')  # 渲染index.html
async def index(request):
    # print(">>>>>>>>>>>", request.args)
    name = request.args.get('title', 'World')
    # 在有与数据库的交互的地方使用await
    post = await Post.create(title=name)  # 插入数据库
    print(await Post.filter(title=name).first())  # 从数据库中获取第一条展示
    return {'post': post}
