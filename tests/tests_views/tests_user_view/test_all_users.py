from flask.testing import FlaskClient


def test_all_users(app_client: FlaskClient):
    response = app_client.get("/users")
    assert response.status_code == 200


def test_get_one_user(app_client: FlaskClient, test_token):
    headers = {
        **test_token,
    }
    response = app_client.get("/users/self", headers=headers)
    assert response.status_code == 200
