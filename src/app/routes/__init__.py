from flask import Flask
from src.app.controllers.user import users
from src.app.controllers.comment import comments

def routes(app: Flask):
    app.register_blueprint(users)
    app.register_blueprint(comments)