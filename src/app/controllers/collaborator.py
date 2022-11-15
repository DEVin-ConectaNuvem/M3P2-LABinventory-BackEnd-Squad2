from flask import Blueprint
from flask.wrappers import Response
from flask import request, jsonify
from bson import json_util
from pymongo import ASCENDING, DESCENDING
from src.app import mongo_client
from src.app.middlewares.auth import required_fields, has_logged

collabs = Blueprint("collabs", __name__,  url_prefix="/collabs")

@collabs.route("/", methods = ["GET"])
def get_all_collabs():
    collabs = mongo_client.collabs.find()
    return Response(
    response=json_util.dumps({'records' : collabs}),
    status=200,
    mimetype="application/json"
  )

@collabs.route("/cadastro", methods=["POST"])
@has_logged()
@required_fields(['nome', 'genero', 'nascimento', 'telefone', 'bairro', 'cargo', 'cep', 'email', 'localidade', 'logradouro', 'numero', 'uf'])
def insert_collabs():
    collabs = request.get_json()
    print(collabs)
    allCollabs = list(mongo_client.collabs.find())
  
    exists = False
    checkEmail = collabs['email']
    for collab in allCollabs:
      if collab['email'] == checkEmail:
        exists = True
    if not exists:
      collabs['id'] = len(allCollabs) + 1
      mongo_client.collabs.insert_one(collabs)
      return {"sucesso": "Colaborador cadastrado com sucesso."}, 201
    if exists:
      return {"erro": "Email já cadastrado."}, 401
    else:
      return {"erro": "Algo deu errado..."}, 500
    
    
@collabs.route("/", methods=["DELETE"])
def delete_all():
    mongo_client.collabs.delete_many({})

    return {"sucesso": "Colaboradores DB limpos com sucesso"}, 204