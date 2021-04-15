from flask import Blueprint, request, current_app
from flask_jwt_extended import (
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
    session = current_app.db.session

    res = request.get_json()
    team_id_1 = res.get("team_id_1")
    team_id_2 = res.get("team_id_2")
    match_winner = res.get("match_winner")
    date = res.get("date")

    new_match = MatchModel(
        team_id_1=team_id_1,
        team_id_2=team_id_2,
        match_winner=match_winner,
        date=date,
    )

    session.add(new_match)

    session.commit()
    return {
        "match": {
            "team_id_1": new_match.team_id_1,
            "team_id_2": new_match.team_id_2,
            "match_winner": new_match.match_winner,
            "date": new_match.date,
        }
    }, HTTPStatus.CREATED


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
