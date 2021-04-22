from threading import settrace
from app.models.team_model import TeamModel
from flask import Blueprint, request, current_app
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from http import HTTPStatus
from datetime import timedelta

from app.models.game_model import GameModel


bp_game = Blueprint("game_view", __name__, url_prefix="/games")


@bp_game.route("/", methods=["POST"], strict_slashes=False)
@jwt_required()
def register_game():
    session = current_app.db.session

    res = request.get_json()
    game_name = res.get("game_name")
    game_type = res.get("game_type")
    game_description = res.get("game_description")

    new_game = GameModel(
        game_name=game_name,
        game_type=game_type,
        game_description=game_description,
    )

    session.add(new_game)

    session.commit()

    return {
        "game": {
            "game_name": new_game.game_name,
            "game_type": new_game.game_type,
            "game_description": new_game.game_description,
        }
    }, HTTPStatus.CREATED


@bp_game.route("/", methods=["GET"], strict_slashes=False)
@jwt_required()
def list_games():

    list_of_games: GameModel = GameModel.query.all()

    return {
        "games": [
            {
                "id": game.id,
                "game_name": game.game_name,
                "game_type": game.game_type,
                "game_description": game.game_description,
            }
            for game in list_of_games
        ]
    }, HTTPStatus.OK


@bp_game.route("/get/<int:game_id>", methods=["GET"], strict_slashes=False)
@jwt_required()
def get_game(game_id):

    found_game: GameModel = GameModel.query.get(game_id)

    if not found_game:
        return {"msg": "Enter a valid game ID"}, HTTPStatus.BAD_REQUEST

    return {
        "game": {
            "id": found_game.id,
            "game_name": found_game.game_name,
            "game_type": found_game.game_type,
            "game_description": found_game.game_description,
        }
    }, HTTPStatus.OK


@bp_game.route("/<int:game_id>", methods=["PATCH"], strict_slashes=False)
@jwt_required()
def update_game(game_id):

    session = current_app.db.session

    body: dict = request.get_json()

    found_game: GameModel = GameModel.query.filter_by(id=game_id).first()

    if not found_game:
        return {"msg": "Insert a valid game ID"}

    for key, value in body.items():
        setattr(found_game, key, value)

    session.add(found_game)
    session.commit()

    return {
        "game": {
            "id": found_game.id,
            "game_name": found_game.game_name,
            "game_type": found_game.game_type,
            "game_description": found_game.game_description,
        }
    }, HTTPStatus.OK
