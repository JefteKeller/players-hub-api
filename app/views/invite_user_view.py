from flask import Blueprint, request, current_app
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)
from http import HTTPStatus

from app.models.team_model import TeamModel
from app.models.team_user_model import TeamUserModel
from app.models.invite_user_model import InviteUserModel


bp_invite_user = Blueprint("invite_user_view", __name__, url_prefix="/invites")


@bp_invite_user.route(
    "/teams/<int:team_id>/send", methods=["POST"], strict_slashes=False
)
@jwt_required()
def invite_player_to_a_team(team_id):
    session = current_app.db.session
    res = request.get_json()
    user_id = res.get("user_id")
    owner_id = get_jwt_identity()

    verify_team_owner: TeamModel = TeamModel.query.filter_by(id=team_id).first()

    if verify_team_owner.owner_id != owner_id:
        return {"error": "You are not the team's owner!"}, HTTPStatus.FORBIDDEN

    verify_player_invite = InviteUserModel.query.filter_by(team_id=team_id).all()

    for invite in verify_player_invite:
        if invite.user_id == user_id:
            return {"error": "This invite is already made!"}, HTTPStatus.FORBIDDEN

    verify_player_in_team = TeamUserModel.query.filter_by(team_id=team_id).all()

    for team_user in verify_player_in_team:
        if team_user.user_id == user_id:
            return {
                "error": "This player is already in this team!"
            }, HTTPStatus.FORBIDDEN

    new_player_invited = InviteUserModel(user_id=user_id, team_id=team_id)

    session.add(new_player_invited)

    session.commit()

    return {
        "invite_made": {
            "user_name": new_player_invited.user.nickname,
            "team_name": new_player_invited.team.team_name,
            "team_owner_name": verify_team_owner.owner.nickname,
        }
    }, HTTPStatus.CREATED


@bp_invite_user.route(
    "/teams/<int:team_id>/accept", methods=["POST"], strict_slashes=False
)
@jwt_required()
def accept_invite(team_id):
    session = current_app.db.session
    res = request.get_json()
    accept_invite = res.get("accept_invite")
    user_id = get_jwt_identity()

    invite: InviteUserModel = (
        InviteUserModel.query.filter_by(user_id=user_id)
        .filter_by(team_id=team_id)
        .first()
    )

    if not invite:
        return {"error": "There isn't any invite for this team"}, HTTPStatus.FORBIDDEN

    team_name = invite.team.team_name

    session.delete(invite)
    session.commit()

    if not accept_invite:
        return {"message": f"The invite from team {team_name} were rejected"}

    new_user_in_team = TeamUserModel(user_id=user_id, team_id=team_id)

    session.add(new_user_in_team)
    session.commit()

    return {
        "Message": f"user {new_user_in_team.user.nickname} joined in team {new_user_in_team.team.team_name}"
    }, HTTPStatus.OK


@bp_invite_user.route("/users/self", methods=["GET"], strict_slashes=False)
@jwt_required()
def get_user_invites():
    user_id = get_jwt_identity()

    invites: InviteUserModel = InviteUserModel.query.filter_by(user_id=user_id).all()

    if not invites:
        return {
            "error": "There isn't invites of any team for you!"
        }, HTTPStatus.NOT_FOUND

    teams = [invite.team for invite in invites]

    return {
        "user_teams_invites": [
            {
                "team_name": team.team_name,
                "team_description": team.team_description,
                "team_created_date": team.team_created_date,
                "team_owner": team.owner.nickname,
            }
            for team in teams
        ]
    }, HTTPStatus.OK
