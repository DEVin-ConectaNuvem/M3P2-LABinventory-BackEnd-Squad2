def create_collection_comments(mongo_client):
    comments_validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["_id","name", "email", "movie_id", "text", "date"],
            "properties": {
                "_id": {
                  "bsonType": "objectId",
                  "description": "Chave definida da collection"
                },
                "name": {
                  "bsonType": "string",
                  "description": "Nome do usuário",
                },
                "email": {
                  "bsonType": "string",
                  "description": "Duração",
                },
                "movie_id": {
                  "bsonType": "objectId",
                  "description": "Vínculo da collection movie"
                },
                "text": {
                  "bsonType": "string",
                  "description": "Comentário",
                },
                "date": {
                  "bsonType": "date",
                  "description": "Data do comentário"
                }
            },
        }
    }

    try:
        mongo_client.create_collection("comments")
    except Exception as e:
        print(e)

    mongo_client.command("collMod", "comments", validator=comments_validator)

