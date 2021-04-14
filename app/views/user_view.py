from flask import Blueprint, request, current_app
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from http import HTTPStatus
from datetime import timedelta

from app.models.user_model import UserModel


bp_user = Blueprint("user_view", __name__, url_prefix="/users")
bp_register = Blueprint("register_view", __name__, url_prefix="/register")
bp_login = Blueprint("login_view", __name__, url_prefix="/login")


@bp_register.route("/", methods=["POST"])
def register():
    session = current_app.db.session

    res = request.get_json()
    nickname = res.get("nickname")
    first_name = res.get("first_name")
    last_name = res.get("last_name")
    biography = res.get("biography")
    created_at = res.get("created_at")
    email = res.get("email")
    password = res.get("password")

    verify_user: UserModel = UserModel.query.filter_by(email=email).first()

    if verify_user:
        return {"msg": f"{email} already exists"}, HTTPStatus.FORBIDDEN

    new_user = UserModel(
        nickname=nickname,
        email=email,
        first_name=first_name,
        last_name=last_name,
        biography=biography,
        created_at=created_at,
    )
    new_user.password = password
    session.add(new_user)

    session.commit()

    access_token = create_access_token(
        identity=new_user.id, expires_delta=timedelta(days=7)
    )

    return {
        "user": {
            "email": new_user.email,
            "nickname": new_user.nickname,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "biography": new_user.biography,
            "created_at": new_user.created_at,
            "access_token": access_token,
        }
    }, HTTPStatus.CREATED


@bp_login.route("/", methods=["POST"])
def login():
    res = request.get_json()
    email = res.get("email")
    password = res.get("password")

    found_user: UserModel = UserModel.query.filter_by(email=email).first()

    if not found_user or not found_user.check_password(password):
        return {"msg": "Incorrect user or password"}, HTTPStatus.UNAUTHORIZED

    access_token = create_access_token(
        identity=found_user.id, expires_delta=timedelta(days=7)
    )
    return {"accessToken": access_token}, HTTPStatus.OK


@bp_user.route("/self", methods=["GET"])
@jwt_required()
def get_user():

    user_id = get_jwt_identity()
    logged_user: UserModel = UserModel.query.filter_by(id=user_id).first()

    if not logged_user:
        return {"msg": "You are not logged in!"}, HTTPStatus.NOT_FOUND

    return {"msg": logged_user.first_name}, HTTPStatus.OK


@bp_user.route("/self", methods=["DELETE"])
@jwt_required()
def delete_user():
    session = current_app.db.session

    user_id = get_jwt_identity()
    user_to_be_deleted: UserModel = UserModel.query.filter_by(id=user_id).first()

    if not user_to_be_deleted:
        return {"msg": f"You are not logged in!"}, HTTPStatus.NOT_FOUND

    session.delete(user_to_be_deleted)
    session.commit()

    return {"msg": f"{user_to_be_deleted.email} deleted"}, HTTPStatus.OK


@bp_user.route("/self", methods=["PATCH", "PUT"])
@jwt_required()
def update_user():
    return {"msg": "Teste update user"}, HTTPStatus.OK
