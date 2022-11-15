
from functools import wraps
from flask import request, jsonify
from src.app import mongo_client


def has_logged():
    def jwt_required(function_current):
        @wraps(function_current)
        def wrapper(*args, **kwargs):
            token = None
            token = request.headers.get("Authorization")
            
            if token:
                return function_current(*args, **kwargs)
            else:
                return jsonify({"error": "Você não está logado"}), 403

        return wrapper
    return jwt_required

def user_exists():
    def _user_exists(function_current):
        @wraps(function_current)
        def __user_exists(*args, **kwargs):
            user = request.get_json()

            search = mongo_client.users.find_one({"email": user['email']})

            if not search:
                return function_current(*args, **kwargs)
            return jsonify({"error": f"Usuário {user['email']} já existe."})
        return __user_exists
    return _user_exists

