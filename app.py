from src.app import app
from src.app.routes import routes


routes(app)

if __name__ == "__main__":
    app.run()