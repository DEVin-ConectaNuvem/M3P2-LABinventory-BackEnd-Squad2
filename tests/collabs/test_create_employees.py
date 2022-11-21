import random

from flask import json


def test_create_employee_failed_not_logged(client):
    data = {
        "id": 99,
        "nome": "Tonho da Lua",
        "genero": "Masculino",
        "nascimento": "1993-02-01",
        "telefone": "(48) 99999-6688",
        "bairro": "Verde Mar",
        "cargo": "Fullstack dev",
        "cep": "11677-246",
        "complemento": "89",
        "email": "tonho@email.com",
        "localidade": "Caraguatatuba",
        "logradouro": "Rua Quinze",
        "numero": "55",
        "referencia": "escultura de areia",
        "uf": "SP"
    }

    response = client.post("collabs/cadastro", data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    
    assert response.status_code == 403
    assert response.json['error'] == "Você não está logado"


def test_create_employee_success(client, logged_in_client):
    data = {
        "id": 99,
        "nome": "Tonho da Lua",
        "genero": "Masculino",
        "nascimento": "1993-02-01",
        "telefone": "(48) 99999-6688",
        "bairro": "Verde Mar",
        "cargo": "Fullstack dev",
        "cep": "11677-246",
        "complemento": "89",
        "email": "tonho@email.com",
        "localidade": "Caraguatatuba",
        "logradouro": "Rua Quinze",
        "numero": "55",
        "referencia": "escultura de areia",
        "uf": "SP"
    }

    response = client.post("collabs/cadastro", data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {logged_in_client}"
    })
    
    assert response.status_code == 201
    assert response.json['sucesso'] == "Colaborador cadastrado com sucesso."


def test_create_employee_failed_already_exists(client, logged_in_client):
    data = {
        "id": 99,
        "nome": "Tonho da Lua",
        "genero": "Masculino",
        "nascimento": "1993-02-01",
        "telefone": "(48) 99999-6688",
        "bairro": "Verde Mar",
        "cargo": "Fullstack dev",
        "cep": "11677-246",
        "complemento": "89",
        "email": "tonho@email.com",
        "localidade": "Caraguatatuba",
        "logradouro": "Rua Quinze",
        "numero": "55",
        "referencia": "escultura de areia",
        "uf": "SP"
    }

    response = client.post("collabs/cadastro", data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {logged_in_client}"
    })
    
    assert response.status_code == 400
    assert response.json['error'] == "Colaborador com email tonho@email.com já existe."


def test_create_employee_failed_missing_field(client, logged_in_client):
    keys = ['nome', 'genero', 'nascimento', 'telefone', 'bairro', 'cargo', 'cep', 'email', 'localidade', 'logradouro', 'numero', 'uf']
    keys_not_have_in_request = keys.pop(random.randrange(len(keys)))

    data = {
        "id": 98,
        "nome": "Rutinha",
        "genero": "Feminino",
        "nascimento": "1993-02-01",
        "telefone": "(48) 99999-6678",
        "bairro": "Verde Mar",
        "cargo": "Fullstack dev",
        "cep": "11677-246",
        "complemento": "89",
        "email": "rutinha@email.com",
        "localidade": "Caraguatatuba",
        "logradouro": "Rua Quinze",
        "numero": "55",
        "referencia": "escultura de areia",
        "uf": "SP"
    }

    del data[keys_not_have_in_request]

    response = client.post("collabs/cadastro", data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {logged_in_client}"
    })
    
    assert response.status_code == 400
    assert f"Faltando campos: ['{keys_not_have_in_request}']" in response.json["error"]
