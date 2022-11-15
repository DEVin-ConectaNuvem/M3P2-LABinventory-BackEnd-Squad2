import os
from flask import Flask
from src.app.config import app_config
from src.app.swagger import create_swagger
from flask_cors import CORS
from src.app.utils import client
from src.app.models.movies import create_collection_movies
from src.app.models.comments import create_collection_comments


app = Flask(__name__)
app.config.from_object(app_config[os.getenv("FLASK_ENV")])

create_swagger(app)
mongo_client = client["devinventory"]


create_collection_movies(mongo_client=mongo_client)
create_collection_comments(mongo_client=mongo_client)

CORS(app)

