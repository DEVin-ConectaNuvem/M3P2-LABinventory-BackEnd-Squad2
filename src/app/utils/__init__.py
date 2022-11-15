import os
import certifi
from pymongo import MongoClient


client = MongoClient(os.getenv("MONGO_URI"), tls=True, tlsCAFile=certifi.where())