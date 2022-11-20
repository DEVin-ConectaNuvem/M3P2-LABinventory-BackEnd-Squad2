import random

from flask import json


def test_create_user_success(client):
    data = {
        "name": "João do Caminhão",
        "email": "joao@email.com",
        "password": "Abcd1234"
    }

    response = client.post("users/create", data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    
    assert response.status_code == 201
    assert response.json['sucesso'] == "User inserido com sucesso"


def test_create_user_failed_already_exists(client):
    data = {
        "name": "João do Caminhão",
        "email": "joao@email.com",
        "password": "Abcd1234"
    }

    response = client.post("users/create", data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    
    assert response.status_code == 401
    assert response.json['error'] == "Usuário joao@email.com já existe."


def test_create_user_failed_missing_field(client):
    keys = ["name", "email", "password"]
    keys_not_have_in_request = keys.pop(random.randrange(len(keys)))

    data = {
        "name": "João do Caminhão",
        "email": "joaoc@email.com",
        "password": "Abcd1234"
    }

    del data[keys_not_have_in_request]

    response = client.post("users/create", data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    
    assert response.status_code == 400
    assert f"Faltando campos: ['{keys_not_have_in_request}']" in response.json["error"]


def test_create_user_failed_weak_password(client):
    data = {
        "name": "João do Caminhão",
        "email": "joao_c@email.com",
        "password": "Abc123"
    }

    response = client.post("users/create", data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    
    assert response.status_code == 400
    assert response.json['error'] == "A senha deve ser maior que 8 dígitos"


def test_create_user_failed_wrong_email_address(client):
    data = {
        "name": "João do Caminhão",
        "email": "joao_email.com",
        "password": "Abcd1234"
    }

    response = client.post("users/create", data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    
    assert response.status_code == 400
    assert response.json['error'] == "O email não é valido"
