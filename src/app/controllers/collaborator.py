
from flask import Blueprint
from flask.wrappers import Response
from src.app import mongo_client
from bson import json_util
# from pymongo import ASCENDING, DESCENDING
from flask import request, jsonify
from src.app.utils import get_collabs_by_name


collabs = Blueprint("collabs", __name__,  url_prefix="/collabs")

@collabs.route("/", methods = ["GET"])
def get_all_collabs():

    name = request.args.get('name')
    # page = request.args.get('page', 1, type=int)
    # limit = 10
    # skip = limit * (page - 1)
    if name:
        list_collabs_per_name = get_collabs_by_name(name)
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