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


@bp_user.route("/", methods=["PATCH"], strict_slashes=False)
@jwt_required()
def update_user():

    user_id = get_jwt_identity()
    found_user: UserModel = UserModel.query.get(user_id)

    if not found_user:
        return {"error": "User not found"}, HTTPStatus.BAD_REQUEST

    data = request.get_json()

    new_nickname = data.get("nickname")
    new_first_name = data.get("first_name")
    new_last_name = data.get("last_name")
    new_password = data.get("password")
    new_email = data.get("email")
    new_biography = data.get("biography")

    if new_email:
        found_user.email = new_email

    if new_password:
        found_user.password = new_password

    if new_nickname:
        found_user.nickname = new_nickname

    if new_first_name:
        found_user.first_name = new_first_name

    if new_last_name:
        found_user.last_name = new_last_name

    if new_biography:
        found_user.biography = new_biography

    session = current_app.db.session
    session.add(found_user)
    session.commit()

    return {
        "user": {
            "email": found_user.email,
            "nickname": found_user.nickname,
            "first_name:": found_user.first_name,
            "last_name": found_user.last_name,
            "biography": found_user.biography,
        }
    }, HTTPStatus.OK


@bp_user.route("/", methods=["GET"])
def users_list():
    username_filter = request.args.get("nickname")

    if username_filter:
        list_of_users = (
            UserModel.query.filter(UserModel.nickname.like(f"%{username_filter}%"))
            .order_by(UserModel.nickname)
            .all()
        )
    else:
        list_of_users = UserModel.query.all()

    return {
        "users": [
            {
                "id": user.id,
                "nickname": user.nickname,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "biography": user.biography,
            }
            for user in list_of_users
        ]
    }, HTTPStatus.OK
