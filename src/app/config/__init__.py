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
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")

class Development(Config):
    TESTING = False 
    DEBUG = True
    MONGO_URI = "mongodb+srv://mayconrcampos:tZa66W2iubEEHDS@cluster0.fbj6hbc.mongodb.net/devinventory/?retryWrites=true&w=majority"

class Production(Config):
    TESTING = False 
    DEBUG = False
    MONGO_URI = "mongodb+srv://mayconrcampos:tZa66W2iubEEHDS@cluster0.fbj6hbc.mongodb.net/devinventory-prod/?retryWrites=true&w=majority"
   
class Testing(Config):
    DEBUG = False
    TESTING = True
    MONGO_URI = "mongodb+srv://mayconrcampos:tZa66W2iubEEHDS@cluster0.fbj6hbc.mongodb.net/devinventory-test/?retryWrites=true&w=majority"

class Homologation(Config):
    DEBUG = False
    TESTING = False
    MONGO_URI = "mongodb+srv://mayconrcampos:tZa66W2iubEEHDS@cluster0.fbj6hbc.mongodb.net/devinventory-homo/?retryWrites=true&w=majority"

app_config = {
    "development": Development,
    "production": Production,
    "testing": Testing,
    "homologation": Homologation
}