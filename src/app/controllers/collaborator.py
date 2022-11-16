
from flask import Blueprint
from flask.wrappers import Response
from src.app.middlewares.auth import has_logged
from src.app import mongo_client
from bson import json_util
# from pymongo import ASCENDING, DESCENDING
from flask import request, jsonify

collabs = Blueprint("collabs", __name__,  url_prefix="/collabs")

@collabs.route("/", methods = ["GET"])
@has_logged()
def get_all_collabs():

    name = request.args.get('name')
    if name:
        list_collabs_per_name = mongo_client.collabs.find({"nome": { "$regex": name}})
        if not list_collabs_per_name:
            error = {
                "Error": "Usuário não encontrado."
            }
            return jsonify(error), 204

        return Response(
            response=json_util.dumps({"records": list_collabs_per_name}),
            status=200,
            mimetype="application/json")

    collabs = mongo_client.collabs.find()
    return Response(
    response=json_util.dumps({'records' : collabs}),
    status=200,
    mimetype="application/json"
  )

@collabs.route("/", methods=["POST"])
def insert_collabs():
    collabs = request.get_json()

    mongo_client.collabs.insert_one(collabs)

    return {"sucesso": f"Colaborador inserido com sucesso"}, 201
    
@collabs.route("/", methods=["DELETE"])
def delete_all():
    mongo_client.collabs.delete_many({})

    return {"sucesso": "Colaboradores DB limpos com sucesso"}, 204