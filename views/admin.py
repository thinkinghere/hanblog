from sanic import Blueprint
from ext import mako, auth
from models import Post
from config import PER_PAGE

bp = Blueprint('admin', url_prefix='/admin')


@bp.route('/')
@auth.login_required
@mako.template('admin/index.html')
async def index(request):
    name = request.args.get('title', 'World')
    await Post.create(title=name)
    print(await Post.filter(title=name).first())
    return {}


@bp.route('/posts')
@auth.login_required
@mako.template('admin/index.html')
async def list_posts(request):
    return {}


@bp.route('/posts/new')
@auth.login_required
@mako.template('admin/index.html')
async def new_post(request):
    return {}


@bp.route('/pages')
@auth.login_required
@mako.template('admin/index.html')
async def list_pages(request):
    return {}


@bp.route('/pages/new')
@auth.login_required
@mako.template('admin/index.html')
async def new_pages(request):
    return {}


@bp.route('/users')
@auth.login_required
@mako.template('admin/list_users.html')
async def list_users(request):
    return {}


@bp.route('/users/new', methods=['GET', 'POST'])
@auth.login_required
async def new_user(request):
    return {}
