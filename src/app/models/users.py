def create_collection_users(mongo_client):
    users_validator = {
      "$jsonSchema": {
          "bsonType": "object",
          "required": [ 
            "_id",
            "name",
            "email",
            "password"
          ],
        }
    }

    try:
      mongo_client.create_collection("users")
    except Exception as e:
      print(e)

    mongo_client.command("collMod", "users", validator=users_validator)