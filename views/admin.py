from sanic import Blueprint
from ext import mako, auth
from models import Post, User
from config import PER_PAGE
from forms import UserForm
from models.user import generate_password
from sanic_mako import render_template

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
    """
    创建用户
    :param request:
    :return:
    """
    return await _user(request)


async def _user(request, user_id=None):
    """
    用户创建 or 更新
    :param request:
    :param user_id:
    :return:
    """
    form = UserForm(request)  # 创建用户form 对象
    msg = ''  # 用户前端页面显示创建成功后显示的内容

    if user_id is not None:
        user = await User.get_or_404(user_id)  # base models

    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        active = form.active.data
        user = await User.filter(name=name).first()  # search user
        if user:
            user.email = email
            if password:
                user.password = generate_password(password)
            user.active = active
            await user.save()
            msg = 'User was successfully updated.'
        else:
            user = await User.create(name=name, email=email,
                                     password=password, active=active)
            msg = 'User was successfully created.'
        users = await User.all()
        total = await User.filter().count()
        context = {'users': users, 'total': total, 'msg': msg}
        # 获取全部的用户并跳转到用户列表
        return await render_template('admin/list_users.html', request, context)
    elif user_id is not None:  # GET 的编辑页面
        form = UserForm(request, obj=user)
        form.password.data = ''
        form.active.data = user.active
        form.submit.label.text = 'Update'
    return await render_template('admin/user.html', request,{'form': form, 'msg': msg, 'user_id': user_id})


@bp.route('/user/<user_id>/edit', methods=['GET', 'POST'])
@auth.login_required
async def edit_user(request, user_id=None):
    return await _user(request, user_id=user_id)
