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
    return {"msg": "Teste list games"}, HTTPStatus.OK


@bp_game.route("/get/", methods=["GET"], strict_slashes=False)
@jwt_required()
def get_game():
    return {"msg": "Teste get game"}, HTTPStatus.OK


@bp_game.route("/", methods=["PATCH"], strict_slashes=False)
@jwt_required()
def update_game():
    return {"msg": "Teste update game"}, HTTPStatus.OK
