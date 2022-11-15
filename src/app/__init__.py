import os
from flask import Flask
from src.app.config import app_config
from src.app.swagger import create_swagger
from flask_cors import CORS
from src.app.utils import mongo
from src.app.models.users import create_collection_users
from src.app.models.items import create_collection_items
from src.app.models.collaborators import create_collection_collaborators
#from src.app.models.comments import create_collection_comments
#DB = mongo(url=os.getenv("MONGO_URI"))

app = Flask(__name__)
app.config.from_object(app_config[os.getenv("FLASK_ENV")])

create_swagger(app)
mongo.init_app(app)
mongo_client = mongo.cx.get_database("devinventory")


create_collection_users(mongo_client=mongo_client)
create_collection_items(mongo_client=mongo_client)
create_collection_collaborators(mongo_client=mongo_client)
#create_collection_comments(mongo_client=mongo_client)

CORS(app)

