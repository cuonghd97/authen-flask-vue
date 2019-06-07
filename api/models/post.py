from sqlalchemy import exc

from db import db


class PostModel(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(200), nullable=False)

    def add_post(self):
        db.session.add(self)
        db.session.commit()
