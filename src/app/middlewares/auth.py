
from functools import wraps
from flask import request, jsonify


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