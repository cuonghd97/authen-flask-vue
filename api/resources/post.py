from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity, get_raw_jwt

from models.post import PostModel
import error.error as error

parser = reqparse.RequestParser()


class Post(Resource):
    @jwt_required
    def post(self):
        parser.add_argument("title", help="Title can't be blank", required=True)
        parser.add_argument("content", help="Content can't be blank", required=True)

        postData = parser.parse_args()

        new_post = PostModel(title=postData["title"], content=postData["content"])
        # new_post = PostModel(title="title", content="content")

        try:
            new_post.add_post()

            return {"message": "Create post sucessfully"}
        except Exception as e:
            print(e)

            return {"message": "Get error when create post"}

    @jwt_required
    def get(self):
        return {"message": "All posts"}
