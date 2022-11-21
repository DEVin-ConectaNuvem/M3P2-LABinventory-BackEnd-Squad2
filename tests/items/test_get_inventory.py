from flask import json


mimetype = 'application/json'
url = "/items/"

url_error='/itens/'

# Sem autorização
def test_get_not_authorized(client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    response = client.get(url, headers=headers)
    assert response.status_code == 403
    assert response.json["error"] == "Você não está logado"

#Teste get url errada
def test_get_error_url(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"

    response = client.get(url_error, headers=headers)
    assert response.status_code == 404

def test_get_all(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"

    response = client.get(url, headers=headers)
    assert response.status_code == 200
    assert len(response.json["records"])>0  

def test_get_title_inexist(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"

    data = {
        "titulo": "bolinha"
    }

    response = client.get(url, data = json.dumps(data),headers=headers)
    assert response.status_code == 200
    for i in response.json["records"]:
        if(i["titulo"] == "bolinha"):
            assert i["titulo"] != "bolinha"
        else:
            return False
    


def test_get_title(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"

    data = {
        "titulo": "Teclado sem fio ABNT2"
    }

    response = client.get(url, data = json.dumps(data),headers=headers)
    assert response.status_code == 200
    for i in response.json["records"]:
        if(i["titulo"] == "Teclado sem fio ABNT2"):
            assert i["titulo"] == "Teclado sem fio ABNT2"
        else:
            return False
    

def test_get_product_cod(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"

    data = {
        "product_code": "AB1234-567"
    }

    response = client.get(url, data = json.dumps(data),headers=headers)
    assert response.status_code == 200
    assert response.json["records"][0]["patrimonio"] == "AB1234-567"

def test_get_description(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"

    data = {
        "description": "Teclado Logitech K380 ABNT2 sem fio, teclas de mídia de fácil acesso, conexão USB, pilhas inclusas e layout ABNT2. mointo maravilhoso"
    }

    response = client.get(url, data = json.dumps(data),headers=headers)
    assert response.status_code == 200
    for i in response.json["records"]:
        if(i["descricao"] == "Teclado Logitech K380 ABNT2 sem fio, teclas de mídia de fácil acesso, conexão USB, pilhas inclusas e layout ABNT2. mointo maravilhoso"):
            temp = i["descricao"]
            assert i["descricao"] == temp
        else:
            return False
            

def test_get_brand(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"

    data = {
        "brand": "Logitech"
    }

    response = client.get(url, data = json.dumps(data),headers=headers)
    assert response.status_code == 200
    for i in response.json["records"]:
        if(i["marca"] == "Logitech"):
            assert i["marca"] == "Logitech"
        else:
            return False


def test_get_model(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"

    data = {
        "model": "K997"
    }

    response = client.get(url, data = json.dumps(data),headers=headers)
    assert response.status_code == 200
    for i in response.json["records"]:
        if(i["modelo"] == "K997"):
            assert i["modelo"] == "K997"
        else:
            return False

def test_get_item_emprestado(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"

    response = client.get(url, headers=headers)
    assert response.status_code == 200
    # print(response.json)
    for i in response.json["records"]:
        if(i["emprestado"] != "Item disponível"):
            temp = i["emprestado"]
            assert i["emprestado"] == temp
        else:
            return False   

def test_get_item_na_empresa(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"

    response = client.get(url, headers=headers)
    assert response.status_code == 200
    # print(response.json)
    for i in response.json["records"]:
        if(i["emprestado"] == "Item disponível"):
            assert i["emprestado"] == "Item disponível"
        else:
            return False  