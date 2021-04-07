from sanic import Blueprint, response
from ext import mako, auth
from forms import LoginForm
from models.user import validate_login
from sanic_mako import render_template


bp = Blueprint('index', url_prefix='/')


@bp.route('/login', methods=['GET', 'POST'])
async def login(request):
    form = LoginForm(request)
    error = ''
    if request.method == 'POST' and form.validate():
        name = form.name.data
        password = form.password.data
        is_validated, user = await validate_login(name, password)
        if is_validated:
            auth.login_user(request, user)
            return response.redirect(request.app.url_for('admin.index'))
        error = 'Validation failed. Please try again'
    return await render_template('admin/login_user.html', request, {'form': form, 'error': error})


@bp.route('logout')
@auth.login_required
async def log_out(request):
    auth.logout_user(request)
    return response.redirect(request.app.url_for('index.login'))
