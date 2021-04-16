from flask import Flask
from flask.cli import AppGroup

from ..services import (
    populate_users,
    populate_teams,
    populate_games,
    populate_matches,
    populate_locations,
    populate_teams_users,
)
from ..models import (
    UserModel,
    TeamModel,
    GameModel,
    MatchModel,
    LocationModel,
    TeamUserModel,
)


def init_app(app: Flask):
    session = app.db.session

    cli_db_group = AppGroup("db_cli")
    cli_user_group = AppGroup("user")
    cli_team_group = AppGroup("team")
    cli_game_group = AppGroup("game")
    cli_match_group = AppGroup("match")
    cli_location_group = AppGroup("location")
    cli_team_user_group = AppGroup("team_user")

    @cli_db_group.command("create")
    def cli_db_create_all():
        app.db.create_all()

    @cli_db_group.command("drop")
    def cli_db_drop_all():
        app.db.drop_all()

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

    @cli_user_group.command("delete_all")
    def cli_user_delete():
        all_users = session.query(UserModel).paginate().items

        for user in all_users:
            session.delete(user)
            session.commit()

    @cli_team_group.command("create")
    def cli_team_create():
        for team in populate_teams:
            new_team = TeamModel(
                team_name=team["team_name"],
                team_description=team["team_description"],
                owner_id=team["owner_id"],
            )

            session.add(new_team)
            session.commit()

    @cli_team_group.command("delete_all")
    def cli_team_delete_all():
        all_teams = session.query(TeamModel).paginate().items

        for team in all_teams:
            session.delete(team)
            session.commit()

    @cli_game_group.command("create")
    def cli_game_create():
        for game in populate_games:
            new_game = GameModel(
                game_name=game["game_name"],
                game_type=game["game_type"],
                game_description=game["game_description"],
            )

            session.add(new_game)
            session.commit()

    @cli_match_group.command("create")
    def cli_match_create():
        for match in populate_matches:
            new_match = MatchModel(
                match_winner=match["match_winner"],
                team_id_1=match["team_id_1"],
                team_id_2=match["team_id_2"],
                date=match["date"],
                game_id=match["game_id"],
                location_id=match["location_id"],
            )

            session.add(new_match)
            session.commit()

    @cli_location_group.command("create")
    def cli_location_create():
        for location in populate_locations:
            new_location = LocationModel(
                location_name=location["location_name"],
                location_phone=location["location_phone"],
            )

            session.add(new_location)
            session.commit()

    @cli_team_user_group.command("create")
    def cli_team_user_create():
        for relation in populate_teams_users:
            new_relation = TeamUserModel(
                user_id=relation["user_id"],
                team_id=relation["team_id"],
            )

            session.add(new_relation)
            session.commit()

    app.cli.add_command(cli_db_group)
    app.cli.add_command(cli_user_group)
    app.cli.add_command(cli_team_group)
    app.cli.add_command(cli_game_group)
    app.cli.add_command(cli_match_group)
    app.cli.add_command(cli_location_group)
    app.cli.add_command(cli_team_user_group)
