from datetime import datetime
from flask import Blueprint
from flask.wrappers import Response
from src.app import mongo_client
from bson import json_util
from pymongo import ASCENDING, DESCENDING

movies = Blueprint("movies", __name__,  url_prefix="/movies")

@movies.route("/", methods = ["GET"])
def get_all_movies():
  movies = mongo_client.movies.aggregate([
    {
        # Inner Join entre tabelas
        '$lookup': {
            'from': 'comments', 
            'localField': '_id', 
            'foreignField': 'movie_id', 
            'as': 'comments'
        }
    }, {                                                                                                                       
        # filtros
        '$match': {
            'comments': {
                '$ne': []
            }, 
            "genres": {
                    "$in": ["Drama"]
                },
            #"tomatoes": {
            #    "$exists": True
            #}
            "released": {
                "$lte": datetime.strptime("1990-01-01", "%Y-%m-%d"),
                "$gte": datetime.strptime("1989-01-01", "%Y-%m-%d")
            }
     
        }
    }, 
    {
        # Indica as casas que eu quero que apareça no resultado
        '$project': {
            "_id": 0,
            "year": 1,
            "title": 1,
            "writers": 1,
            "released": 1,
            # define um aliase para genres
            "generows": "$genres"
        }
    }, 
    {
      "$limit": 100
    },
    {
        "$sort": {
            "released": ASCENDING
        }
    }
  ])
  #movies = mongo_client.movies.find().limit(200)

  return Response(
    response=json_util.dumps({'records' : movies}),
    status=200,
    mimetype="application/json"
  )