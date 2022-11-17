import os
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())

class Config:
    FLASK_ENV = os.getenv('FLASK_ENV')
    FLASK_APP = os.getenv('FLASK_APP')
    SECRET_KEY = os.getenv('SECRET_KEY')
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    OAUTHLIB_INSECURE_TRANSPORT = os.getenv('OAUTHLIB_INSECURE_TRANSPORT')
    FRONTEND_URL = os.getenv("FRONTEND_URL")
    BACKEND_URL = os.getenv('BACKEND_URL')
    MONGO_URI = os.getenv("MONGO_URI")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")

class Development(Config):
    TESTING = False 
    DEBUG = True

class Production(Config):
    TESTING = False 
    DEBUG = False
   
class Testing(Config):
    DEBUG = False
    TESTING = True

class Homologation(Config):
    DEBUG = False
    TESTING = False

app_config = {
    "development": Development,
    "production": Production,
    "testing": Testing,
    "homologation": Homologation
}