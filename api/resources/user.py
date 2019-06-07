import os

from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    # jwt_manager,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt,
)
from flask import request
from werkzeug.utils import secure_filename
# from flask_cors import cross_origin

from models.user import UserModel
from models.revoke import RevokedTokenModel
import error.error as error
from config import Config

parser = reqparse.RequestParser()


class UserRegister(Resource):
    def post(self):
        parser.add_argument(
            "username",
            help="Username can not be none",
            required=True
        )
        parser.add_argument(
            "password",
            help="Password can not be none",
            required=True
        )

        postData = parser.parse_args()

        if UserModel.find_by_username(postData["username"]):
            return error.ALREADY_EXISTS

        new_user = UserModel(
            username=postData["username"],
            password=UserModel.hash_pass(postData["password"]),
        )

        try:
            new_user.save_to_db()
            access_token = create_access_token(identity=postData["username"])
            refresh_token = create_refresh_token(identity=postData["username"])

            return {
                "message": "Register success",
                "access_token": access_token,
                "refresh_token": refresh_token,
            }
        except Exception as e:
            print(e)
            return error.SERVER_ERROR_500


class UserLogin(Resource):
    def post(self):
        parser.add_argument(
            "username",
            help="Username can not be none",
            required=True
        )
        parser.add_argument(
            "password",
            help="Password can not be none",
            required=True
        )

        postData = parser.parse_args()

        current_user = UserModel.find_by_username(postData["username"])

        if not current_user:
            return error.DOES_NOT_EXIST

        if not UserModel.check_pass(postData["password"],
                                    current_user.password):
            return error.WRONG_PASSWORD

        access_token = create_access_token(identity=current_user.username)
        refresh_token = create_refresh_token(identity=current_user.username)

        return {
            "message": "Login success",
            "access_token": access_token,
            "refresh_token": refresh_token,
        }


class UserProfile(Resource):
    @jwt_required
    def put(self):
        parser.add_argument("fullname")
        # postData = parser.parse_args()

        current_user = get_jwt_identity()

        extensions = set(["png", "jpg", "jpeg"])
        try:
            file = request.files["avatar"]
        except Exception as e:
            print(e)
            return error.INVALID_INPUT_422

        filename = file.filename
        if filename.rsplit(".", 1)[1].lower() not in extensions:
            return error.INVALID_INPUT_422
        path = os.path.join(Config.UPLOAD_FOLDER, secure_filename(filename))
        print(path)
        file.save(path)

        user = UserModel.find_by_username(str(current_user))
        UserModel.update(path=path, user=user)
        print(user)
        return {"message": "upload"}

    @jwt_required
    def get(self):
        print(request.headers)
        username = get_jwt_identity()
        return UserModel.get_one_user(str(username))

    @jwt_required
    def post(self):
        return {"message": "post"}


class LogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()["jti"]
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()

            return {"message": "Token has been revoked"}
        except Exception as e:
            print(e)

            return {"message": "Something went wrong"}


class LogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()["jti"]
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()

            return {"message": "Refresh token has been revoked"}
        except Exception as e:
            print(e)

            return {"message": "Some thing went wrong"}
