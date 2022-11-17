from functools import wraps
from flask import request, jsonify
from src.app import mongo_client

def item_exists():
    def _item_exists(function_current):
        @wraps(function_current)
        def __item_exists(*args, **kwargs):
            item = request.get_json()

            search = mongo_client.items.find_one({"patrimonio": item['patrimonio']})

            if not search:
                return function_current(*args, **kwargs)
            return jsonify({"error": f"Já existe um item cadastrado com o patrimônio {item['patrimonio']}."}), 401
        return __item_exists
    return _item_exists