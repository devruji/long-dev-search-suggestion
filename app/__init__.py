import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect

from app.extensions import db


# ?: Application Factory

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config.from_object(cls_config_selector())

    # ?: Install Extensions
    install_extensions(app)

    # ?: Register Blueprints
    register_blueprints(app)

    return app


# ?: Helper Functions


def cls_config_selector():
    env = os.getenv("FLASK_ENV", "development")
    match env:
        case "development":
            return "config.DevelopmentConfig"
        case "production":
            return "config.ProductionConfig"
        case _:
            return "config.DevelopmentConfig"


def install_extensions(app):
    db.init_app(app)
    csrf.init_app(app)


def register_blueprints(app):
    from app.main import main_bp
    from app.search import search_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(search_bp)
