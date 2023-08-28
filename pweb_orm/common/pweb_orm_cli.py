from flask.cli import AppGroup, with_appcontext
from ppy_common.ppyc_console_log import Console

pweb_orm_cli = AppGroup("db-cli", help="PWeb App Database Manipulation")
_pweb_orm_cli_db = None
_DB_CONFIG_NOT_FOUND = 'Database Configuration Not Found'


@pweb_orm_cli.command("init", help="Initialize database tables")
@with_appcontext
def initialize():
    if _pweb_orm_cli_db:
        _pweb_orm_cli_db.create_all()
        Console.blue('Successfully Initialize Database & Tables', bold=True, system_log=True)
    else:
        Console.blue(_DB_CONFIG_NOT_FOUND, bold=True, system_log=True)


@pweb_orm_cli.command("destroy", help="Delete database tables")
@with_appcontext
def destroy():
    if _pweb_orm_cli_db:
        _pweb_orm_cli_db.drop_all()
        Console.green('Successfully Delete Database Tables', system_log=True, bold=True)
    else:
        Console.blue(_DB_CONFIG_NOT_FOUND, system_log=True, bold=True)


def init_pweb_orm_cli(app, db):
    global _pweb_orm_cli_db
    _pweb_orm_cli_db = db
    if app:
        app.cli.add_command(pweb_orm_cli)
