
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

def has_not_logged():
    def _has_not_logged(function_current):
        @wraps(function_current)
        def __has_not_logged(*args, **kwargs):
            token = None
            token = request.headers.get("Authorization")
            
            if not token:
                return function_current(*args, **kwargs)
            else:
                return jsonify({"error": "Você já está logado"}), 401
        return __has_not_logged
    return _has_not_logged

def user_exists():
    def _user_exists(function_current):
        @wraps(function_current)
        def __user_exists(*args, **kwargs):
            user = request.get_json()

            search = mongo_client.users.find_one({"email": user['email']})

            if not search:
                return function_current(*args, **kwargs)
            return jsonify({"error": f"Usuário {user['email']} já existe."}), 401
        return __user_exists
    return _user_exists

def required_fields(fields: list):
    def _required_fields(function_current):
        @wraps(function_current)
        def __required_fields(*args, **kwargs):
            body = request.get_json()

            faul = False
            campos = []
            for field in fields:
                if not field in body:
                    faul = True
                    campos.append(field)
                    
            if not faul:
                return function_current(*args, **kwargs)
            return jsonify({"error": f"Faltando campos: {campos}"}), 400
        return __required_fields
    return _required_fields

