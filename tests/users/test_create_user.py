from flask import json

mimetype = 'application/json'
url = '/users/create'

def test_missing_fields(client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "email": "julia@email.com",
        "password": "@abc1234"
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltando campos: ['name']"

def test_create_existing_user(client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "name": "Julia Moura",
        "email": "julia@email.com",
        "password": "@abc1234"
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 401
    assert response.json["error"] == "Usuário julia@email.com já existe."   

# def test_create_user(client): 
#     headers = {
#         'Content-Type': mimetype,
#         'Accept': mimetype
#     }
#     data = {
#         "name": "Julia Moura",
#         "email": "julia.moura@email.com",
#         "password": "@abc1234"
#     }
#     response = client.post(url, data=json.dumps(data), headers=headers)
#     assert response.status_code == 201
#     assert response.json["error"] == "Usuário julia@email.com já existe."