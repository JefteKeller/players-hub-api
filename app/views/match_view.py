from flask import Blueprint, request, current_app
from flask_jwt_extended import jwt_required
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
    date = res.get("date")

    new_match = MatchModel(
        team_id_1=team_id_1,
        team_id_2=team_id_2,
        game_id=game_id,
        date=date,
    )

    session.add(new_match)

    session.commit()

    match = match_serializer(new_match)

    return match, HTTPStatus.CREATED


@bp_match.route("/", methods=["GET"], strict_slashes=False)
@jwt_required()
def list_matches():
    match_list = MatchModel.query.all()
    res = []

    for match in match_list:
        res.append(match_serializer(match))

    return {"Matches": res}, HTTPStatus.OK


@bp_match.route("/<int:match_id>", methods=["GET"], strict_slashes=False)
@jwt_required()
def get_match(match_id):
    match: MatchModel = MatchModel.query.get(match_id)

    match_return = match_serializer(match)

    return {"Match": match_return}, HTTPStatus.OK


@bp_match.route("/<int:match_id>", methods=["PATCH"], strict_slashes=False)
@jwt_required()
def update_match(match_id):
    session = current_app.db.session

    sent_updated_match = request.get_json()

    date = sent_updated_match.get("date")
    match_winner_id = sent_updated_match.get("match_winner_id")
    team_id_1 = sent_updated_match.get("team_id_1")
    team_id_2 = sent_updated_match.get("team_id_2")

    match_to_update: MatchModel = MatchModel.query.filter_by(id=match_id).update(
        dict(
            date=date,
            match_winner_id=match_winner_id,
            team_id_1=team_id_1,
            team_id_2=team_id_2,
        )
    )

    if not match_to_update:
        return {"Error": "Match not found"}, HTTPStatus.NOT_FOUND

    session.commit()

    match: MatchModel = MatchModel.query.get(match_id)
    match_return = match_serializer(match)

    return {"Match": match_return}, HTTPStatus.OK
