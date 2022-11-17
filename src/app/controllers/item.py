from flask import Blueprint, request
from flask.wrappers import Response
from src.app import mongo_client
from bson import json_util
from pymongo import ASCENDING, DESCENDING
from src.app.middlewares.auth import required_fields, has_logged
from src.app.middlewares.items import item_exists


items = Blueprint("items", __name__,  url_prefix="/items")

@items.route("/", methods = ["GET"])
def get_all_items():
    items = mongo_client.items.find()
    return Response(
    response=json_util.dumps({'records' : items}),
    status=200,
    mimetype="application/json"
  )

@items.route("/create", methods=["POST"])
@has_logged()
@required_fields(["patrimonio", "titulo", "categoria", "valor", "marca", "modelo", "descricao", "url"])
@item_exists()
def insert_item():
    item = request.get_json()

    item['emprestado'] = "Item disponível"

    mongo_client.items.insert_one(item)

    return {"sucesso": "Item cadstrado com sucesso"}, 201
    
@items.route("/", methods=["DELETE"])
def delete_all():
    mongo_client.items.delete_many({})

    return {"sucesso": "Items limpos com sucesso"}, 200