from functools import wraps
from flask import request, jsonify
from src.app import mongo_client

def collab_exists():
    def _collab_exists(function_current):
        @wraps(function_current)
        def __collab_exists(*args, **kwargs):
            collab = request.get_json()

            search = mongo_client.collabs.find_one({"email": collab['email']})

            if not search:
                return function_current(*args, **kwargs)
            return jsonify({"error": f"Colaborador com email {collab['email']} já existe."}), 401
        return __collab_exists
    return _collab_exists