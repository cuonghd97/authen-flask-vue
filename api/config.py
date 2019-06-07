import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = "cc"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'jwt-secret-string'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=24)

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    Folder = os.path.join(APP_ROOT, "{}".format("upload"))

    if not os.path.isdir(Folder):
        os.mkdir(Folder)

    UPLOAD_FOLDER = Folder
