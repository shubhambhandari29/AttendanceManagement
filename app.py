from flask import Flask
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from config import Config
from routes import init_routes

jwt = JWTManager()
mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    mongo.init_app(app)
    print(f"Mongo URI: {app.config['MONGO_URI']}")  # Debugging statement
    jwt.init_app(app)
  

    with app.app_context():
        init_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
