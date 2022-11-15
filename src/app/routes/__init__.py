from flask import Flask
from src.app.controllers.user import users
from src.app.controllers.item import items
from src.app.controllers.collaborator import collabs

def routes(app: Flask):
    app.register_blueprint(users)
    app.register_blueprint(items)
    app.register_blueprint(collabs)