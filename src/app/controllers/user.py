
from flask import Blueprint
from flask.wrappers import Response
from src.app import mongo_client
from bson import json_util
#from pymongo import ASCENDING, DESCENDING
from flask import request, jsonify, current_app
from src.app.utils import set_password, validate_password, generate_jwt, check_valid_email
from datetime import datetime, timedelta, timezone
from src.app.middlewares.auth import has_logged, user_exists, required_fields, has_not_logged
from flask.globals import session
from google import auth
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import os
import json
from werkzeug.utils import redirect
import requests


users = Blueprint("users", __name__,  url_prefix="/users")

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

flow = Flow.from_client_secrets_file(
    client_secrets_file="src/app/utils/client_secret.json",
    scopes=[
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
        "openid",
    ],
    redirect_uri="http://localhost:5000/users/callback",
)

@users.route("/", methods = ["GET"])
@has_logged()
def get_all_users():
    users = mongo_client.users.find()
    return Response(
    response=json_util.dumps({'records' : users}),
    status=200,
    mimetype="application/json"
  )

@users.route("/create", methods=["POST"])
@required_fields(["name", "email", "password"])
@user_exists()
def insert_user():
    try:
        user = request.get_json()
        if check_valid_email(user["email"]) and len(user["password"]) >= 8:
            payload = {
                "name": user['name'],
                "email": user["email"],
                "password": set_password(user["password"])
            }

            mongo_client.users.insert_one(payload)
            return {"sucesso": f"User inserido com sucesso"}, 201
        else:
            if not check_valid_email(user["email"]):
                return {"error": "O email não é valido"}, 400
            if len(user["password"]) < 8:
                return {"error": "A senha deve ser maior que 8 dígitos"}, 400
    except Exception as exp:
        print(exp.args)
        return {"error": "Document failed validation"}, 400
    
@users.route("/", methods=["DELETE"])
@has_logged()
def delete_all():
    mongo_client.users.delete_many({})

    return {"sucesso": "Usuários limpos com sucesso"}, 200

@users.route("/login", methods=["POST"])
@has_not_logged()
@required_fields(["email", "password"])
def login_user():
    user_request = request.get_json()
    
    try:
        user = mongo_client.users.find_one({"email" : user_request['email']})

        if not user or not validate_password(user['password'], user_request['password']):
            return {"error": "Suas credenciais estão incorretas!", "status_code": 401},401

        payload = {
            "name": user['name'],
            "email": user['email'],
            "exp": datetime.now(tz=timezone.utc) + timedelta(days=1),
        }
        token = generate_jwt(payload)

        return {
            "token": token,
            "name": user['name'],
            "email": user['email'], 
            "status_code": 200}, 200

    except Exception as e:
        return {"error": f"{e}"}


@users.route("/auth/google", methods=["POST"])
def auth_google():
    authorization_url, state = flow.authorization_url()
    session["state"] = state

    return Response(
          response=json.dumps({"url": authorization_url}),
          status=200,
          mimetype="application/json",
        )


@users.route("/callback", methods=["GET"])
def callback():
    flow.fetch_token(authorization_response=request.url)
    credentials = flow.credentials
    request_session = requests.session()
    token_google = auth.transport.requests.Request(session=request_session)

    user_google_dict = id_token.verify_oauth2_token(
        id_token=credentials.id_token,
        request=token_google,
        audience=current_app.config["GOOGLE_CLIENT_ID"],
    )
    email = user_google_dict["email"]
    name = user_google_dict["name"]
    user = mongo_client.users.find_one({"email": email})

    if not user:
        new_user = {
            'name': name,
            'email': email,
            'password': set_password("abcd12345"),
        }
        user = mongo_client.users.insert_one(new_user)
    
    #user_google_dict["roles"] = ["READ", "WRITE"]
    session["google_id"] = user_google_dict.get("sub")
    del user_google_dict["aud"]
    del user_google_dict["azp"]

    token = generate_jwt(user_google_dict)

    return redirect(f"{current_app.config['FRONTEND_URL']}#/users/{token}/{name}")