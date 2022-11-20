import random

from flask import json


def test_user_login_success(client):
    data = {
        "email": "mcoelho@email.com",
        "password": "@abc1234"
    }

    response = client.post('users/login', data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    })

    assert response.status_code == 200
    assert "token" in response.json


def test_user_login_failed_already_logged(client, logged_in_client):
    data = {
        "email": "mcoelho@email.com",
        "password": "@abc1234"
    }

    response = client.post('users/login', data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {logged_in_client}"
    })

    assert response.status_code == 401
    assert response.json["error"] == "Você já está logado"


def test_user_login_failed_user_not_exist(client):
    data = {
        "email": "julia.moura",
        "password": "123"
    }

    response = client.post('users/login', data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    })

    assert response.status_code == 401
    assert response.json["error"] == "Suas credenciais estão incorretas!"


def test_user_login_failed_wrong_password(client):
    data = {
        "email": "mcoelho@email.com",
        "password": "123"
    }

    response = client.post('users/login', data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    })

    assert response.status_code == 401
    assert response.json["error"] == "Suas credenciais estão incorretas!"


def test_user_login_failed_missing_fields(client):
    keys = ["email", "password"]
    keys_not_have_in_request = keys.pop(random.randrange(len(keys)))

    data = {
        "email": "mcoelho@email.com",
        "password": "@abc1234"
    }

    del data[keys_not_have_in_request]

    response = client.post('users/login', data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    })

    assert response.status_code == 400
    assert response.json["error"] == "Faltando campos: ['password']"
