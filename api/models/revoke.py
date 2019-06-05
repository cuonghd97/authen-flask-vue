from db import db
from sqlalchemy import exc


class RevokedTokenModel(db.Model):
    __tablename__ = "revoked_token"
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(200))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_revoked(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
