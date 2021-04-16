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
    cli_all_data_group = AppGroup("all_data")

    def create_user():
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

    def delete_all_user():
        all_users = session.query(UserModel).paginate().items

        for user in all_users:
            session.delete(user)
            session.commit()

    def create_team():
        for team in populate_teams:
            new_team = TeamModel(
                team_name=team["team_name"],
                team_description=team["team_description"],
                owner_id=team["owner_id"],
            )

            session.add(new_team)
            session.commit()

    def delete_all_team():
        all_teams = session.query(TeamModel).paginate().items

        for team in all_teams:
            session.delete(team)
            session.commit()

    def create_game():
        for game in populate_games:
            new_game = GameModel(
                game_name=game["game_name"],
                game_type=game["game_type"],
                game_description=game["game_description"],
            )

            session.add(new_game)
            session.commit()

    def create_match():
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

    def create_location():
        for location in populate_locations:
            new_location = LocationModel(
                location_name=location["location_name"],
                location_phone=location["location_phone"],
            )

            session.add(new_location)
            session.commit()

    def create_team_user():
        for relation in populate_teams_users:
            new_relation = TeamUserModel(
                user_id=relation["user_id"],
                team_id=relation["team_id"],
            )

            session.add(new_relation)
            session.commit()

    def create_all_data():
        create_user()
        create_team()
        create_game()
        create_location()
        create_match()
        create_team_user()

    @cli_db_group.command("create")
    def cli_db_create_all():
        app.db.create_all()
        print("All tables created")

    @cli_db_group.command("drop")
    def cli_db_drop_all():
        app.db.drop_all()
        print("All tables dropped")

    @cli_user_group.command("create")
    def cli_user_create():
        create_user()

    @cli_user_group.command("delete_all")
    def cli_user_delete():
        delete_all_user()

    @cli_team_group.command("create")
    def cli_team_create():
        create_team()

    @cli_team_group.command("delete_all")
    def cli_team_delete_all():
        delete_all_team()

    @cli_game_group.command("create")
    def cli_game_create():
        create_game()

    @cli_match_group.command("create")
    def cli_match_create():
        create_match()

    @cli_location_group.command("create")
    def cli_location_create():
        create_location()

    @cli_team_user_group.command("create")
    def cli_team_user_create():
        create_team_user()

    @cli_all_data_group.command("restart")
    def cli_all_data_restart():
        app.db.drop_all()
        print("All tables dropped!")

        app.db.create_all()
        print("All tables created!")

        create_all_data()
        print("All data created in tables!")

    app.cli.add_command(cli_db_group)
    app.cli.add_command(cli_user_group)
    app.cli.add_command(cli_team_group)
    app.cli.add_command(cli_game_group)
    app.cli.add_command(cli_match_group)
    app.cli.add_command(cli_location_group)
    app.cli.add_command(cli_team_user_group)
    app.cli.add_command(cli_all_data_group)
