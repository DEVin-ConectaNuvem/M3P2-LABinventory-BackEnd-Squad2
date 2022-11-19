import pytest
# from src.app import create_app
from src.app import create_app
from src.app.routes import routes
from flask import json

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}

@pytest.fixture(scope="session")
def app():
    app_on = create_app('testing')['app']
    routes(app_on)
    return app_on

@pytest.fixture
def create_user_in_client(client):
    data = {
        "name": "Marcelo Coelho",
        "email": "mcoelho@email.com",
        "password": "@abc1234"
    }
    response = client.post("users/create", data=json.dumps(data), headers=headers)
    return response

@pytest.fixture
def logged_in_client(client):
    data = {
        "email": "mcoelho@email.com",
        "password": "@abc1234"
    }

    response = client.post("users/login", data=json.dumps(data), headers=headers)
    return response.json["token"]


