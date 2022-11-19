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

mongo_client = mongo[os.getenv('MONGO_DATABASE')]

def create_app(environment):

    app = Flask(__name__)
    app.config.from_object(app_config[environment])
    CORS(app)
    # app.config.update(
    #     TESTING=True,
    #     SECRET_KEY=os.getenv("SECRET_KEY")
    # )
    create_swagger(app)

    db = {"development": "devinventory", "testing": "devinventory-test", "production": "devinventory-prod", "homologation": "devinventory-homo"}
    
    mongo_client = mongo[db[environment]]
    
    create_collection_users(mongo_client=mongo_client)
    create_collection_items(mongo_client=mongo_client)
    create_collection_collaborators(mongo_client=mongo_client)
    
    return {"app": app, "mongo_client": mongo_client}
#create_collection_comments(mongo_client=mongo_client)


