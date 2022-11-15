from flask import Flask
from src.app.controllers.movie import movies
from src.app.controllers.comment import comments

def routes(app: Flask):
    app.register_blueprint(movies)
    app.register_blueprint(comments)