import random

from flask import json


url = "items/"

def test_create_item_failed_not_logged(client):
    response = client.post(url)
    
    assert response.status_code == 403
    assert response.json['error'] == "Você não está logado"


def test_create_item_success(client, logged_in_client):
    data = { 
        "patrimonio": "XY6532-121",
        "titulo": "Roteador Wireless TP-Link",
        "categoria": "Acessórios",
        "valor": 289.00,
        "url": "https://images.tcdn.com.br/img/img_prod/740836/roteador_wireless_tp_link_ac1200_mbps_dual_band_archer_c6_4_antenas_10383_1_5f06f26b623e06989965d36bdc2ba9bc.jpg",
        "marca": "TP-Link",
        "modelo": "AC1200",
        "descricao": "Roteador Wireless TP-Link AC1200 4 antenas",
        "emprestado": "Item disponível"
    }

    response = client.post(url, data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {logged_in_client}"
    })
    
    assert response.status_code == 201
    assert response.json['sucesso'] == "Item cadstrado com sucesso"


def test_create_item_failed_already_exists(client, logged_in_client):
    data = { 
        "patrimonio": "XY6532-121",
        "titulo": "Roteador Wireless TP-Link",
        "categoria": "Acessórios",
        "valor": 289.00,
        "url": "https://images.tcdn.com.br/img/img_prod/740836/roteador_wireless_tp_link_ac1200_mbps_dual_band_archer_c6_4_antenas_10383_1_5f06f26b623e06989965d36bdc2ba9bc.jpg",
        "marca": "TP-Link",
        "modelo": "AC1200",
        "descricao": "Roteador Wireless TP-Link AC1200 4 antenas",
        "emprestado": "Item disponível"
    }

    response = client.post(url, data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {logged_in_client}"
    })
    
    assert response.status_code == 400
    assert response.json['error'] == "Já existe um item cadastrado com o patrimônio XY6532-121."


def test_create_item_failed_missing_field(client, logged_in_client):
    keys = ["patrimonio", "titulo", "categoria", "valor", "marca", "modelo", "descricao", "url"]
    keys_not_have_in_request = keys.pop(random.randrange(len(keys)))

    data = { 
        "patrimonio": "XY6532-000",
        "titulo": "Roteador Wireless TP-Link",
        "categoria": "Acessórios",
        "valor": 289.00,
        "url": "https://images.tcdn.com.br/img/img_prod/740836/roteador_wireless_tp_link_ac1200_mbps_dual_band_archer_c6_4_antenas_10383_1_5f06f26b623e06989965d36bdc2ba9bc.jpg",
        "marca": "TP-Link",
        "modelo": "AC1200",
        "descricao": "Roteador Wireless TP-Link AC1200 4 antenas",
        "emprestado": "Item disponível"
    }

    del data[keys_not_have_in_request]

    response = client.post(url, data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {logged_in_client}"
    })

    assert response.status_code == 400
    assert f"Faltando campos: ['{keys_not_have_in_request}']" in response.json["error"]


def test_create_item_failed_wrong_value(client, logged_in_client):
    data = { 
        "patrimonio": "XY6532-999",
        "titulo": "Roteador Wireless TP-Link",
        "categoria": "Acessórios",
        "valor": 0.00,
        "url": "https://images.tcdn.com.br/img/img_prod/740836/roteador_wireless_tp_link_ac1200_mbps_dual_band_archer_c6_4_antenas_10383_1_5f06f26b623e06989965d36bdc2ba9bc.jpg",
        "marca": "TP-Link",
        "modelo": "AC1300",
        "descricao": "Roteador Wireless TP-Link AC1300 6 antenas",
        "emprestado": "Item disponível"
    }

    response = client.post(url, data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {logged_in_client}"
    })
    
    assert response.status_code == 400
    assert response.json['error'] == "Valor tem que ser maior que zero"
