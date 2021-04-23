from app.models.team_model import TeamModel
from flask import Blueprint, request, current_app
from flask_jwt_extended import jwt_required

from http import HTTPStatus

from app.models.match_model import MatchModel
from app.serializers.match_serializer import match_serializer


bp_match = Blueprint("match_view", __name__, url_prefix="/matches")


@bp_match.route("/", methods=["POST"], strict_slashes=False)
@jwt_required()
def register_match():
    session = current_app.db.session

    data = request.get_json()

    found_team_1 = TeamModel.query.filter_by(id=data.get("team_id_1", 0)).first()
    found_team_2 = TeamModel.query.filter_by(id=data.get("team_id_2", 0)).first()

    if not found_team_1 or not found_team_2:
        return {"error": "Not found some of the specified Teams"}, HTTPStatus.NOT_FOUND

    try:
        new_match = MatchModel(
            team_id_1=data["team_id_1"],
            team_id_2=data["team_id_2"],
            game_id=data["game_id"],
            date=data["date"],
        )
    except KeyError:
        return {
            "error": "Missing Keys, check the body of the request"
        }, HTTPStatus.BAD_REQUEST

    session.add(new_match)

    session.commit()

    match = match_serializer(new_match)

    return match, HTTPStatus.CREATED


@bp_match.route("/", methods=["GET"], strict_slashes=False)
@jwt_required()
def list_matches():
    match_list = MatchModel.query.all()

    all_matches = [match_serializer(match) for match in match_list]

    return {"matches": all_matches}, HTTPStatus.OK


@bp_match.route("/<int:match_id>", methods=["GET"], strict_slashes=False)
@jwt_required()
def get_match(match_id):
    found_match: MatchModel = MatchModel.query.filter_by(id=match_id).first()

    if not found_match:
        return {"error": "Match not found"}, HTTPStatus.NOT_FOUND

    match_return = match_serializer(found_match)

    return {"match": match_return}, HTTPStatus.OK


@bp_match.route("/<int:match_id>", methods=["PATCH"], strict_slashes=False)
@jwt_required()
def update_match(match_id):
    session = current_app.db.session

    data = request.get_json()

    match_to_update: MatchModel = MatchModel.query.filter_by(id=match_id).first()

    if not match_to_update:
        return {"error": "Match not found"}, HTTPStatus.NOT_FOUND

    [setattr(match_to_update, key, value) for key, value in data.items()]

    session.add(match_to_update)
    session.commit()

    match_return = match_serializer(match_to_update)

    return {"match": match_return}, HTTPStatus.OK
