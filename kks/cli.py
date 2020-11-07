import click

from kks.cmd.auth import auth
from kks.cmd.init import init
from kks.cmd.run import run
from kks.cmd.test import test


@click.group()
def cli():
    """KoKoS helper tool"""


cli.add_command(auth)
cli.add_command(init)
cli.add_command(run)
cli.add_command(test)
