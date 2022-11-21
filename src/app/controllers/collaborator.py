from flask import Blueprint
from flask.wrappers import Response
from src.app import mongo_client
from bson import json_util, ObjectId
from flask import request, jsonify
from src.app.middlewares.auth import required_fields, has_logged
from src.app.middlewares.collabs import collab_exists

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

@collabs.route("/collab/", methods = ["GET"])
@has_logged()
def get_one_collab():
    try:
        collab_id = request.args.get("_id")
        collab = mongo_client.collabs.find_one({"_id": ObjectId(collab_id)})
        return Response(
        response=json_util.dumps({'records' : collab}),
        status=200,
        mimetype="application/json"
    )
    except Exception:
      return {"error": "Colaborador não cadastrado."}, 404


@collabs.route("/", methods=["POST"])
@has_logged()
@required_fields(['nome', 'genero', 'nascimento', 'telefone', 'bairro', 'cargo', 'cep', 'email', 'localidade', 'logradouro', 'numero', 'uf'])
@collab_exists()
def insert_collabs():
    try:
      collabs = request.get_json()
      allCollabs = list(mongo_client.collabs.find())
      collabs['id'] = len(allCollabs) + 1
      mongo_client.collabs.insert_one(collabs)
      return {"sucesso": "Colaborador cadastrado com sucesso."}, 201
    except Exception:
      return {"erro": "Algo deu errado..."}, 500
    
@collabs.route("/", methods=["DELETE"])
@has_logged()
def delete_all():
    mongo_client.collabs.delete_many({})

    return {"sucesso": "Colaboradores DB limpos com sucesso"}, 204

@collabs.route("/collab/", methods=["DELETE"])
@has_logged()
def delete_collab():
    try:
        collab_id = request.args.get("_id")
        mongo_client.collabs.delete_one({'_id': ObjectId(collab_id)})
        return {"sucesso": "Colaborador excluido com sucesso"}, 204
    except:
        return {"error": "Algo deu errado."}, 500

@collabs.route("/edit/", methods=['PUT'])
@has_logged()
def edit_collab():
    try:
        collab_id = request.args.get("_id")
        request_params = request.get_json()
        request_params.pop("_id")
        id_call = {"_id" : ObjectId(collab_id)}
        mongo_client.collabs.update_one(id_call, {'$set':request_params})

        return {"sucesso": "Colaborador alterado com sucesso"}, 204
    except Exception:
        return {"error": "Algo deu errado."}, 500