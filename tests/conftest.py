from flask import Flask
from pytest import fixture

from app import create_app
from app.services.helpers import populate_users
from app.models import UserModel


@fixture
def sample_app():
    yield create_app("test")


@fixture
def app_client(sample_app: Flask):

    with sample_app.test_request_context():

        sample_app.db.create_all()
        session = sample_app.db.session

        for user in populate_users:
            new_user = UserModel(
                nickname=user["nickname"],
                first_name=user["first_name"],
                last_name=user["last_name"],
                email=user["email"],
                password=user["password"],
                biography=user["biography"],
            )

            session.add(new_user)
            session.commit()

        session.close()

    yield sample_app.test_client()

    with sample_app.test_request_context():
        all_users = session.query(UserModel).paginate().items

        for user in all_users:
            session.delete(user)
            session.commit()

        session.close()
        sample_app.db.drop_all()
