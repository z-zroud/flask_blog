import click
from flask import Blueprint
from app.plugins import db

cmd_bp = Blueprint('commands', __name__)


@cmd_bp.cli.command('initdb')
@click.option('--drop', is_flag=True, help='Create after drop')
def initdb(drop):
    if drop:
        db.drop_all()
        click.echo('Drop all tables')
    db.create_all()
    click.echo("Init database.") 
