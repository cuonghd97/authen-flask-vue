from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from db import db
from resources.user import *
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)
api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()

@jwt.token_in_blacklist_loader
def check_token(decrypted_token):
    return bool(False)

api.add_resource(UserRegister, "/register")
api.add_resource(UserLogin, "/login")
api.add_resource(UserProfile, '/profile')

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)