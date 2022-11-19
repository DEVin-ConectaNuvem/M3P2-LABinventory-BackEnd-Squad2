def test_get_inventory_analytics_not_logged(client):
    response = client.get('inventory/analytics')
    
    assert response.status_code == 403
    assert response.json['error'] == "Você não está logado"


def test_get_inventory_analytics_logged(client, logged_in_client):
    response = client.get('inventory/analytics', headers={
        "Authorization": f"Bearer {logged_in_client}"
    })
    
    assert response.status_code == 200


def test_get_inventory_analytics_return_all_fields(client, logged_in_client):
    response = client.get('inventory/analytics', headers={
        "Authorization": f"Bearer {logged_in_client}"
    })
    
    assert "Num_Colabs" in response.json
    assert "Num_Items" in response.json
    assert "Valor_Items" in response.json
    assert "Num_Emprestimos" in response.json
