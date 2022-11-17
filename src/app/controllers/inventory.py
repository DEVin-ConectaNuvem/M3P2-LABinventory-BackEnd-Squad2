
from flask import Blueprint
from flask.wrappers import Response
from src.app import mongo_client
from bson import json_util
from pymongo import ASCENDING, DESCENDING
from flask import request, jsonify

inventors = Blueprint("inventors", __name__,  url_prefix="/inventory")

@inventors.route("/analytics", methods = ["GET"])
def get_all_collabs():
    result = dict()
    collabs = mongo_client.collabs.count_documents({})
    responseCollabs=json_util.dumps(collabs)
    result['Num_Colabs'] = int(responseCollabs)
    items = mongo_client.items.count_documents({})
    responseItems=json_util.dumps(items)
    result['Num_Items'] = int(responseItems)
    Valoritems = mongo_client.items.aggregate([
     {
        '$group': {
            '_id': '$groupField', 
            'val': {
                '$sum': '$valor'
            }
        }
    }, {
        '$project': {
            '_id': 0
        }
    }
    ])
    responseValorItems=json_util.dumps(Valoritems)
    indexInicial = responseValorItems.index(':')+2
    indexFinal = len(responseValorItems)-2
    result['Valor_Items'] = round(float(responseValorItems[indexInicial:indexFinal]),2)
    emprestimos = mongo_client.items.count_documents({'emprestado' :{'$ne': 'Item disponível'}})
    responseEmprestimos=json_util.dumps(emprestimos)
    result['Num_Emprestimos'] = int(responseEmprestimos)
    resultFinal = json_util.dumps(result)
    return Response(resultFinal ,status=200,mimetype="application/json")

    
    
 



    
