from flask import Blueprint, request, current_app
from flask_jwt_extended import jwt_required

from http import HTTPStatus

from app.models import CommentModel, MatchModel


bp_comment = Blueprint("comment_view", __name__, url_prefix="/matches")


@bp_comment.route("/<int:match_id>/comments", methods=["GET"], strict_slashes=False)
@jwt_required()
def get_all_comments(match_id):

    found_match = MatchModel.query.filter_by(id=match_id).first()

    if not found_match:
        return {"error": "The specified Match does not exists"}, HTTPStatus.NOT_FOUND

    return {
        "comments": [
            {
                "id": comment.id,
                "text": comment.text,
                "author": comment.author,
                "timestamp": comment.timestamp,
            }
            for comment in found_match.comments
        ]
    }, HTTPStatus.OK


@bp_comment.route("/<int:match_id>/comments", methods=["POST"], strict_slashes=False)
@jwt_required()
def register_comment(match_id):

    found_match = MatchModel.query.filter_by(id=match_id).first()

    if not found_match:
        return {"error": "The specified Match does not exists"}, HTTPStatus.NOT_FOUND

    session = current_app.db.session
    data = request.get_json()

    try:
        new_comment = CommentModel(
            text=data["text"], author=data["author"], match_id=match_id
        )
    except KeyError:
        return {"error": "Missing Keys, check the request body"}, HTTPStatus.BAD_REQUEST

    session.add(new_comment)
    session.commit()

    return {
        "comment": {
            "id": new_comment.id,
            "text": new_comment.text,
            "author": new_comment.author,
        }
    }, HTTPStatus.OK
