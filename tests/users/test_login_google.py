import requests

url = "users/auth/google"


def test_oauth_login_success_generate_url(client):
    response = client.post(url, headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    })

    assert response.status_code == 200
    assert "url" in response.json

 
def test_oauth_login_failed_already_logged(client, logged_in_client):
    response = client.post(url, headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {logged_in_client}"
    })

    assert response.status_code == 401
    assert response.json["error"] == "Você já está logado"


def test_oauth_login_success_open_google_url(client):
    oauth_url = client.post(url, headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    }).json["url"]

    response = requests.get(oauth_url)

    assert response.status_code == 200
    assert "Fazer login usando sua Conta do Google" in response.text
