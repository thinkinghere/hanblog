import click
from tortoise import Tortoise, run_async

from ext import init_db
from models.user import create_user
from tortoise.exceptions import IntegrityError


async def init():
    await init_db(create_db=False)
    await Tortoise._drop_databases()
    await init_db(create_db=True)
    await Tortoise.generate_schemas()


@click.group()
def cli():
    ...


async def _adduser(**kwargs):
    await init_db()
    try:
        user = await create_user(**kwargs)
    except IntegrityError as e:
        click.echo(str(e))
    else:
        click.echo(f'User {user.name} created!!! ID: {user.id}')


@cli.command()
@click.option('--name', required=True, prompt=True)
@click.option('--email', required=False, default=None, prompt=True)
@click.option('--password', required=True, prompt=True, hide_input=True,
              confirmation_prompt=True)
def adduser(name, email, password):
    run_async(_adduser(name=name, password=password, email=email))


@cli.command()
def initdb():
    run_async(init())
    click.echo('Init Finished!')


if __name__ == '__main__':
    cli()
