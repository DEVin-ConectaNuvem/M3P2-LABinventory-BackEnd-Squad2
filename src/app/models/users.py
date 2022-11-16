def create_collection_users(mongo_client):
    users_validator = {
      "$jsonSchema": {
          "bsonType": "object",
          "title": "Validação de usuários",
          "required": [ 
            "_id",
            "name",
            "email",
            "password"
          ],
          "properties": {
            "name": {
              "bsonType": "string",
              "minLength": 3,
              "maxLength": 40,
              "description": "Nome deve ser uma string maior que 3 caracteres e menor que 40"
            },
            "email": {
              "bsonType": "string",
              "description": "Email deve ser válido"
            },
            "password": {
              "bsonType": "string",
              "minLength": 8,
              "description": "Password é obrigatória e deve ser string"
            }
          }
        }
    }

    try:
      mongo_client.create_collection("users")
    except Exception as e:
      print(e)

    mongo_client.command("collMod", "users", validator=users_validator)