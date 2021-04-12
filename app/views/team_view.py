from flask import Blueprint, request, current_app
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from http import HTTPStatus
from datetime import timedelta

from app.models.team_model import TeamModel


bp_team = Blueprint("team_view", __name__, url_prefix="/teams")

@bp_team.route("/", methods=["POST"])
@jwt_required()
def register_team():
    return {"msg": "Teste register team"}, HTTPStatus.OK

@bp_team.route("/", methods=["GET"])
@jwt_required()
def list_teams():
    return {"msg": "Teste list teams"}, HTTPStatus.OK


@bp_team.route("/get/", methods=["GET"])
@jwt_required()
def get_team():
    return {"msg": "Teste get team"}, HTTPStatus.OK


@bp_team.route("/", methods=["PATCH", "PUT"])
@jwt_required()
def update_team():
    return {"msg": "Teste update team"}, HTTPStatus.OK