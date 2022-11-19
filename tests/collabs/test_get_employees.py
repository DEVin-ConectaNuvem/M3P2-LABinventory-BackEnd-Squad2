def test_get_all_employees_not_logged(client):
    response = client.get('collabs/')
    
    assert response.status_code == 403
    assert response.json['error'] == "Você não está logado"


def test_get_all_employees_success(client, logged_in_client):
    assert client.get('collabs/', headers={
        "Authorization": f"Bearer {logged_in_client}"
    }).status_code == 200


def test_get_specific_employee_success(client, logged_in_client):
    assert client.get('collabs/?name=Adriano', headers={
        "Authorization": f"Bearer {logged_in_client}"
    }).status_code == 200


def test_get_specific_employee_not_found(client, logged_in_client):
    response = client.get('collabs/?name=Jojo', headers={
        "Authorization": f"Bearer {logged_in_client}"
    })

    assert response.status_code == 200
    assert response.json['records'] == []


def test_get_specific_employee_return_correct_fields(client, logged_in_client):
    data = {
        "records": [
            {
                "_id": {
                    "$oid": "6373efec3963e50690a97250"
                },
                "nome": "Adriano Matos Meier",
                "genero": "Masculino",
                "nascimento": "1980-02-07",
                "telefone": "(48) 99988-7766",
                "bairro": "Caminho Novo",
                "cargo": "DevOps",
                "cep": "88132-373",
                "complemento": "901A",
                "email": "adriano@email.com",
                "localidade": "Palhoça",
                "logradouro": "Rua Thomé Israel da Silva",
                "numero": "1055",
                "referencia": "Santa Ana Residence",
                "uf": "SC",
                "id": 1
            }
        ]
    }

    response = client.get('collabs/?name=Adriano', headers={
        "Authorization": f"Bearer {logged_in_client}"
    })

    assert response.status_code == 200
    assert response.json == data
