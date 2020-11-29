import click
from tortoise import Tortoise, run_async

from ext import init_db


async def init():
    await init_db(create_db=False)
    await Tortoise._drop_databases()
    await init_db(create_db=True)
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
