import click
from tortoise import Tortoise, run_async

from ext import init as _init


async def init():
    await _init(create_db=False)
    await Tortoise._drop_databases()
    await _init(create_db=True)
    await Tortoise.generate_schemas()


@click.group()
def cli():
    ...


@cli.command()
def initdb():
    run_async(init())
    click.echo('Init Finished!')


if __name__ == '__main__':
    cli()
