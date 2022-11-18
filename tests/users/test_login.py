from flask import json

mimetype = 'application/json'
url = '/users/login'

def test_post_login(client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    data = {
        "email": "mcoelho@email.com",
        "password": "@abc1234"
    }

    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    assert "token" in response.json

def test_missing_fields(client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    data = {
        "email": "julia.moura"
    }

    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltando campos: ['password']"

def test_user_not_exist(client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    data = {
        "email": "julia.moura",
        "password": "123"
    }

    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 401
    assert response.json["error"] == "Suas credenciais estão incorretas!"