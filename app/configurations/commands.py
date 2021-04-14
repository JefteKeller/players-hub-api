from flask import Flask
from flask.cli import AppGroup

from ..services import populate_users
from ..models import UserModel


def init_app(app: Flask):
    session = app.db.session
    cli_db_group = AppGroup("db_cli")

    @cli_db_group.command("create")
    def cli_db_create_all():
        app.db.create_all()

    @cli_db_group.command("drop")
    def cli_db_drop_all():
        app.db.drop_all()

    app.cli.add_command(cli_db_group)

    cli_user_group = AppGroup("user")

    @cli_user_group.command("create")
    def cli_user_create():
        for user in populate_users:
            new_user = UserModel(
                nickname=user["nickname"],
                first_name=user["first_name"],
                last_name=user["last_name"],
                email=user["email"],
                password=user["password"],
                biography=user["biography"],
            )

            session.add(new_user)
            session.commit()

    app.cli.add_command(cli_user_group)
