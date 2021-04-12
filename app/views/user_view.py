from flask import Blueprint, request, current_app
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from http import HTTPStatus
from datetime import timedelta

from app.models.user_model import UserModel


bp_user = Blueprint("user_view", __name__, url_prefix="/users")


@bp_user.route("/signup", methods=["POST"])
def signup():
    return {"msg": "Teste signup"}, HTTPStatus.CREATED


@bp_user.route("/login", methods=["POST"])
def login():
    return {"msg": "Teste login"}, HTTPStatus.OK


@bp_user.route("/", methods=["GET"])
@jwt_required()
def list_users():
    return {"msg": "Teste users"}, HTTPStatus.OK


@bp_user.route("/get/", methods=["GET"])
@jwt_required()
def get_user():
    return {"msg": "Teste get user"}, HTTPStatus.OK


@bp_user.route("/", methods=["PATCH", "PUT"])
@jwt_required()
def update_user():
    return {"msg": "Teste update user"}, HTTPStatus.OK