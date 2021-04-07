from tortoise import fields
from werkzeug.security import check_password_hash, generate_password_hash

from .base import BaseModel


class User(BaseModel):
    email = fields.CharField(max_length=100)
    name = fields.CharField(max_length=100, unique=True)
    password = fields.TextField()
    active = fields.BooleanField(default=True)

    class Meta:
        table = 'users'


async def create_user(**data):
    if 'name' not in data or 'password' not in data:
        raise ValueError('username and password are required.')

    data['password'] = generate_password(data.pop('password'))

    user = await User.create(**data)
    return user


def generate_password(password):
    """
    生成Hash密码
    :param password:
    :return:
    """
    return generate_password_hash(password, method='pbkdf2:sha256')


async def validate_login(name, password):
    """
    校验用户名 密码
    :param name:
    :param password:
    :return:
    """
    user = await User.filter(name=name).first()
    if not user:
        return False, None
    if check_password_hash(user.password, password):
        return True, user
    return False, None

