from flask import Blueprint, request, current_app
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)
from http import HTTPStatus
from datetime import timedelta

from app.models.match_model import MatchModel
from app.serializers.match_serializer import match_serializer


bp_match = Blueprint("match_view", __name__, url_prefix="/matches")


@bp_match.route("/", methods=["POST"], strict_slashes=False)
@jwt_required()
def register_match():
    session = current_app.db.session

    res = request.get_json()
    team_id_1 = res.get("team_id_1")
    team_id_2 = res.get("team_id_2")
    game_id = res.get("game_id")
    match_winner_id = res.get("match_winner_id")
    date = res.get("date")

    new_match = MatchModel(
        team_id_1=team_id_1,
        team_id_2=team_id_2,
        game_id=game_id,
        match_winner_id=match_winner_id,
        date=date,
    )

    session.add(new_match)

    session.commit()

    match = match_serializer(new_match.id)

    return match, HTTPStatus.CREATED


@bp_match.route("/", methods=["GET"], strict_slashes=False)
@jwt_required()
def list_matches():
    match_list = MatchModel.query.all()
    res = []

    for match in match_list:
        res.append(match_serializer(match.id))

    return {"matches": res}, HTTPStatus.OK


@bp_match.route("/<int:match_id>", methods=["GET"], strict_slashes=False)
@jwt_required()
def get_match(match_id):

    match = match_serializer(match_id)

    return {"match": match}, HTTPStatus.OK


@bp_match.route("/", methods=["PATCH"], strict_slashes=False)
@jwt_required()
def update_match():
    return {"msg": "Teste update match"}, HTTPStatus.OK
