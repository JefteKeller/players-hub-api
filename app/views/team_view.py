from app.models.user_model import UserModel
from flask import Blueprint, request, current_app
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)
from http import HTTPStatus
from datetime import timedelta

from app.models.team_model import TeamModel
from app.models.team_user_model import TeamUserModel


bp_team = Blueprint("team_view", __name__, url_prefix="/teams")


@bp_team.route("/", methods=["POST"], strict_slashes=False)
@jwt_required()
def register_team():
    session = current_app.db.session

    res = request.get_json()
    team_name = res.get("team_name")
    team_description = res.get("team_description")
    owner_id = get_jwt_identity()

    new_team = TeamModel(
        team_name=team_name, team_description=team_description, owner_id=owner_id
    )

    session.add(new_team)

    session.commit()

    return {
        "team": {
            "team_name": new_team.team_name,
            "team_description": new_team.team_description,
            "owner_id": new_team.owner_id,
            "team_created_date": new_team.team_created_date,
        }
    }, HTTPStatus.CREATED


@bp_team.route("/<int:team_id>", methods=["POST"], strict_slashes=False)
@jwt_required()
def register_player_in_team(team_id):
    session = current_app.db.session
    res = request.get_json()
    user_id = res.get("user_id")
    owner_id = get_jwt_identity()

    verify_team_owner = TeamModel.query.filter_by(owner_id=owner_id).first()

    if not verify_team_owner:
        return {"msg": "You are not the team's owner!"}, HTTPStatus.FORBIDDEN

    new_player_in_team = TeamUserModel(user_id=user_id, team_id=team_id)

    session.add(new_player_in_team)

    session.commit()

    return {
        "player_in_team": {
            "user_id": new_player_in_team.user_id,
            "team_id": new_player_in_team.team_id,
            "owner_id": owner_id,
        }
    }, HTTPStatus.CREATED


<<<<<<< HEAD
@bp_team.route("/", methods=["GET"])
=======
@bp_team.route("/", methods=["GET"], strict_slashes=False)
@jwt_required()
>>>>>>> 21c325228857ce2cda8a7206b5d32c462523007c
def list_teams():
    list_of_teams = TeamModel.query.all()

    return {
        "teams": [
            {
                "id": team.id,
                "team_name": team.team_name,
                "team_description": team.team_description,
                "team_created_date": team.team_created_date,
            }
            for team in list_of_teams
        ]
    }, HTTPStatus.OK


@bp_team.route("/<int:team_id>/", methods=["GET"], strict_slashes=False)
@jwt_required()
def get_team(team_id):
    found_team: TeamModel = TeamModel.query.get(team_id)
    if found_team:
        return {
            "team": {
                "id": found_team.id,
                "team_name": found_team.team_name,
                "team_description": found_team.team_description,
                "team_created_date": found_team.team_created_date,
            }
        }, HTTPStatus.OK
    return {"msg": "team not found"}, HTTPStatus.NOT_FOUND


@bp_team.route("/", methods=["PATCH"], strict_slashes=False)
@jwt_required()
def update_team():
    return {"msg": "Teste update team"}, HTTPStatus.OK
