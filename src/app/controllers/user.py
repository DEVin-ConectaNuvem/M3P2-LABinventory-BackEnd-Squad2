
from flask import Blueprint
from flask.wrappers import Response
from src.app import mongo_client
from bson import json_util
#from pymongo import ASCENDING, DESCENDING
from flask import request
from src.app.utils import set_password, validate_password, generate_jwt
from datetime import datetime, timedelta, timezone
from src.app.middlewares.auth import has_logged

users = Blueprint("users", __name__,  url_prefix="/users")

@users.route("/", methods = ["GET"])
@has_logged()
def get_all_users():
    users = mongo_client.users.find()
    return Response(
    response=json_util.dumps({'records' : users}),
    status=200,
    mimetype="application/json"
  )

@users.route("/", methods=["POST"])
def insert_user():
    user = request.get_json()

    payload = {
      "name": user['name'],
      "email": user["email"],
      "password": set_password(user["password"])
    }

    mongo_client.users.insert_one(payload)
    
    return {"sucesso": f"User inserido com sucesso"}, 201
    
@users.route("/", methods=["DELETE"])
def delete_all():
    mongo_client.users.delete_many({})

    return {"sucesso": "Usuários limpos com sucesso"}, 200

@users.route("/login", methods=["POST"])
def login_user():
    user_request = request.get_json()
    
    try:
        user = mongo_client.users.find_one({"email" : user_request['email']})

        print(user['password'], user['email'])

        if not user or not validate_password(user['password'], user_request['password']):
            return {"error": "Suas credenciais estão incorretas!", "status_code": 401}

        payload = {
            "name": user['name'],
            "email": user['email'],
            "exp": datetime.now(tz=timezone.utc) + timedelta(days=1),
        }
        token = generate_jwt(payload)

        return {"token": token, "status_code": 200}

    except Exception as e:
        return {"error": f"{e}"}


