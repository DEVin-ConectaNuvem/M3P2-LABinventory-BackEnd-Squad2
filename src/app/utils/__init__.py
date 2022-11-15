from flask_pymongo import PyMongo
from jwt import encode
from flask import current_app
from werkzeug.security import check_password_hash, generate_password_hash

mongo = PyMongo()

def generate_jwt(payload):
    token = encode(payload, current_app.config["SECRET_KEY"], "HS256")

    return token

def set_password(password):
    return generate_password_hash(password)

def validate_password(password_hash, password):
    return check_password_hash(password_hash, password)
