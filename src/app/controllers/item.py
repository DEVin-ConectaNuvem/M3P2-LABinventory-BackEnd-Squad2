
from flask import Blueprint, request, jsonify
from flask.wrappers import Response
from src.app import mongo_client
from bson import json_util, ObjectId
from pymongo import ASCENDING, DESCENDING
from src.app.middlewares.auth import required_fields, has_logged
from src.app.middlewares.items import item_exists


items = Blueprint("items", __name__,  url_prefix="/items")

@items.route("/", methods = ["GET"])
@has_logged()
def get_all_items():
    title = request.args.get('title')
    if title:
        list_items_per_title = mongo_client.items.find({"titulo": { "$regex": title}})
        if not list_items_per_title:
            error = {
                "Error": "Item não encontrado."
            }
            return jsonify(error), 204

        return Response(
            response=json_util.dumps({"records": list_items_per_title}),
            status=200,
            mimetype="application/json")

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
@has_logged()
def delete_all():
    mongo_client.items.delete_many({})

    return {"sucesso": "Items limpos com sucesso"}, 200

@items.route("/", methods=["PATCH"])
@has_logged()
@required_fields(["patrimonio", "titulo", "categoria", "valor", "marca", "modelo", "descricao", "url"])
def edit_item():
    id_item = request.args.get("_id")
    item_novo = request.get_json()

    update_item = mongo_client.items.update_one({"_id": ObjectId(id_item)},
        {
            "$set": {
                        "patrimonio": item_novo['patrimonio'],
                        "titulo": item_novo['titulo'],
                        "categoria": item_novo['categoria'],
                        "valor": float(item_novo['valor']),
                        "url": item_novo['url'],
                        "marca": item_novo['marca'],
                        "modelo": item_novo['modelo'],
                        "descricao": item_novo['descricao'],
                        "emprestado": item_novo['emprestado']
                    }
        })
    if update_item:
        return {"sucesso": f"Item {item_novo['titulo']} atualizado com sucesso"}, 200
    return {"error": "Erro ao tentar atualizar item"}, 401