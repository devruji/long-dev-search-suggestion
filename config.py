import os


class Config:
    ENV = "development"
    HOST = "0.0.0.0"
    PORT = 5000
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(24)
    CSRF_ENABLED = False
    WTF_CSRF_CHECK_DEFAULT = False
    SQLALCHEMY_DATABASE_URI = "postgresql://bossruji:password@localhost/bossruji"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    HOST = "127.0.0.1"
    DEBUG = True


class ProductionConfig(Config):
    ENV = "producton"
