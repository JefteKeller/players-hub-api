from app.models.match_model import MatchModel
from sqlalchemy import or_
from flask.globals import session
from app.models import team_model
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
from app.models.invite_user_model import InviteUserModel


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


@bp_team.route("/", methods=["GET"], strict_slashes=False)
@jwt_required()
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
    return {"error": "Team not found"}, HTTPStatus.NOT_FOUND


@bp_team.route("/<int:team_id>", methods=["PATCH"], strict_slashes=False)
@jwt_required()
def update_team(team_id):

    session = current_app.db.session

    owner_id = get_jwt_identity()

    body: dict = request.get_json()

    found_team: TeamModel = TeamModel.query.filter_by(id=team_id).first()

    if not found_team:
        return {
            "error": "Not found any team that matches the requested ID."
        }, HTTPStatus.NOT_FOUND

    if found_team.owner_id != owner_id:
        return {"error": "You are not the owner of this Team."}, HTTPStatus.FORBIDDEN

    for key, value in body.items():
        setattr(found_team, key, value)

    session.add(found_team)
    session.commit()

    return {
        "team": {
            "team_name": found_team.team_name,
            "team_description": found_team.team_description,
            "owner_id": found_team.owner_id,
            "team_create_date": found_team.team_created_date,
        }
    }, HTTPStatus.OK


@bp_team.route("/self", methods=["DELETE"])
@jwt_required()
def leave_team():
    session = current_app.db.session
    res = request.get_json()
    team_idt = res.get("team_id")
    user_id = get_jwt_identity()

    TeamUserModel.query.filter_by(user_id=user_id, team_id=team_idt).delete()

    session.commit()

    return {"message": "Leave team"}, HTTPStatus.OK


@bp_team.route("/admin/<int:team_id>", methods=["DELETE"])
@jwt_required()
def owner_purge_user(team_id):
    session = current_app.db.session

    res = request.get_json()
    user_idt = res.get("user_id")
    owner_idt = get_jwt_identity()

    excluir_registro = TeamUserModel.query.filter(
        TeamUserModel.team_id == team_id,
        TeamUserModel.user_id == user_idt,
        TeamModel.owner_id == owner_idt,
    ).first()

    try:
        if excluir_registro.team.owner_id == owner_idt:
            session.delete(excluir_registro)
            session.commit()

            return {
                f"the user {excluir_registro.user.nickname} has been expelled": f"{excluir_registro.team.team_name}",
            }, HTTPStatus.OK
        else:
            return {
                "error": "You aren't the owner of the team"
            }, HTTPStatus.UNAUTHORIZED
    except AttributeError:
        return {"error": "Team id or user id incorrects."}, HTTPStatus.NOT_FOUND


@bp_team.route("/<int:team_id>/history", methods=["GET"])
def team_match_history(team_id):
    team_history = MatchModel.query.filter(
        or_(MatchModel.team_id_1 == team_id, MatchModel.team_id_2 == team_id)
    ).all()

    return {
        "matches": [
            {
                "Match ID": info.id,
                "Match date": info.date,
                "Match winner": info.match_winner.team_name,
                "Team 1 ": {
                    "Team ID": info.team_1.id,
                    "Team name": info.team_1.team_name,
                    "Team description": info.team_1.team_description,
                    "Created at": info.team_1.team_created_date,
                },
                "Team 2 ": {
                    "Team ID": info.team_2.id,
                    "Team name": info.team_2.team_name,
                    "Team description": info.team_2.team_description,
                    "Created at": info.team_2.team_created_date,
                },
            }
            for info in team_history
        ]
    }


@bp_team.route("/self/<int:team_id>", methods=["DELETE"])
@jwt_required()
def delete_team(team_id):

    session = current_app.db.session

    owner_id = get_jwt_identity()

    team_to_be_deleted: TeamModel = TeamModel.query.filter_by(
        owner_id=owner_id, id=team_id
    ).first()

    if not team_to_be_deleted:
        return {"error": "Invalid team ID"}, HTTPStatus.NOT_FOUND

    session.delete(team_to_be_deleted)
    session.commit()

    return {"message": f"Deleted team with ID: {team_id}"}, HTTPStatus.OK
