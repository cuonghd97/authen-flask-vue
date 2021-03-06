from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_cors import CORS

from db import db
from resources.user import *
from resources.post import *
from config import Config
from models.revoke import RevokedTokenModel

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
jwt = JWTManager(app)
api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()


@jwt.token_in_blacklist_loader
def check_token_revoked(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_revoked(jti)


# User
api.add_resource(UserRegister, "/register")
api.add_resource(UserLogin, "/login")
api.add_resource(UserProfile, "/profile")
api.add_resource(LogoutAccess, "/logout/access")
api.add_resource(LogoutRefresh, "/logout/refresh")

# Post
api.add_resource(Post, "/modify-post")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
