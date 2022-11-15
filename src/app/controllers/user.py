
from flask import Blueprint
from flask.wrappers import Response
from src.app import mongo_client
from bson import json_util
from pymongo import ASCENDING, DESCENDING
from flask import request, jsonify

users = Blueprint("users", __name__,  url_prefix="/users")

@users.route("/", methods = ["GET"])
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

    mongo_client.users.insert_one(user)

    return {"sucesso": f"User inserido com sucesso"}, 201
    
@users.route("/", methods=["DELETE"])
def delete_all():
    mongo_client.users.delete_many({})

    return {"sucesso": "Usuários limpos com sucesso"}, 200