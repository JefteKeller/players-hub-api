from flask.testing import FlaskClient
from werkzeug.datastructures import Authorization, Headers


def test_delete_user(app_client: FlaskClient, test_token):
    headers = {
        **test_token,
    }
    response = app_client.delete("/users/self", headers=headers)
    assert response.status_code == 200
