from flask import Blueprint, request, current_app
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from http import HTTPStatus
from datetime import timedelta

from app.models.match_model import MatchModel


bp_match = Blueprint("match_view", __name__, url_prefix="/matches")

@bp_match.route("/", methods=["POST"])
@jwt_required()
def register_match():
    return {"msg": "Teste register match"}, HTTPStatus.OK

@bp_match.route("/", methods=["GET"])
@jwt_required()
def list_matches():
    return {"msg": "Teste list matches"}, HTTPStatus.OK


@bp_match.route("/get/", methods=["GET"])
@jwt_required()
def get_match():
    return {"msg": "Teste get match"}, HTTPStatus.OK


@bp_match.route("/", methods=["PATCH", "PUT"])
@jwt_required()
def update_match():
    return {"msg": "Teste update match"}, HTTPStatus.OK