def create_collection_collaborators(mongo_client):
    collaborators_validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["nome", "genero", "nascimento", "telefone", "bairro", "cargo", "cep", "email", "localidade", "logradouro", "uf"],
            "properties": {
                "_id": {
                  "bsonType": "objectId",
                  "description": "Chave definida da collection"
                },
                "nome": {
                  "bsonType": "string",
                  "description": "Nome do colaborador",
                },
                "genero": {
                  "bsonType": "string",
                  "description": "genero",
                },
                "nascimento": {
                  "bsonType": "date",
                  "description": "data nascimento"
                },
                "telefone": {
                  "bsonType": "string",
                  "description": "Fone",
                },
                "bairro": {
                  "bsonType": "string",
                  "description": "Bairro onde mora"
                },
                "cargo": {
                  "bsonType": "string",
                  "description": "Cargo em que trabalha"
                },
                "cep": {
                  "bsonType": "string",
                  "description": "Cep de onde mora"
                },
                "complemento": {
                  "bsonType": "string",
                  "description": "Complemento endereço"
                },
                "email": {
                  "bsonType": "string",
                  "description": "email colaborador"
                },
                "localidade": {
                  "bsonType": "string",
                  "description": "Cidade onde mora"
                },
                "logradouro": {
                  "bsonType": "string",
                  "description": "Rua onde mora"
                },
                "numero": {
                  "bsonType": "int",
                  "description": "Número da residencia"
                },
                "referencia": {
                  "bsonType": "string",
                  "description": "Referência de onde mora"
                },
                "uf": {
                  "bsonType": "string",
                  "description": "Estado da federação"
                },

            },
        }
    }

    try:
        mongo_client.create_collection("collaborators")
    except Exception as e:
        print(e)

    mongo_client.command("collMod", "collaborators", validator=collaborators_validator)