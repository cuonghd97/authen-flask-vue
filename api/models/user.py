import bcrypt
from sqlalchemy import exc

from db import db


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    fullname = db.Column(db.String(200))
    avatar = db.Column(db.String(200))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @staticmethod
    def hash_pass(password):
        return bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())

    @staticmethod
    def check_pass(password, hashed):
        return bcrypt.checkpw(password.encode("utf8"), hashed)

    @classmethod
    def update(cls, **kwargs):
        print(kwargs.items())
        return {"message": "update"}

    @classmethod
    def get_one_user(cls, username):
        def to_json(item):
            return {
                "id": item.id,
                "fullname": item.fullname
            }

        user = cls.query.filter_by(username=username).first()

        return {"user": to_json(user)}