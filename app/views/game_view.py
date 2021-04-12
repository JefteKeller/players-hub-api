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

@bp_game.route("/", methods=["POST"])
@jwt_required()
def register_game():
    return {"msg": "Teste register game"}, HTTPStatus.OK

@bp_game.route("/", methods=["GET"])
@jwt_required()
def list_games():
    return {"msg": "Teste list games"}, HTTPStatus.OK

@bp_game.route("/get/", methods=["GET"])
@jwt_required()
def get_game():
    return {"msg": "Teste get game"}, HTTPStatus.OK


@bp_game.route("/", methods=["PATCH", "PUT"])
@jwt_required()
def update_game():
    return {"msg": "Teste update game"}, HTTPStatus.OK