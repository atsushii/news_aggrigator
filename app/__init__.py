from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("../config.py")

    from .views.views import view_blueprint
    app.register_blueprint(view_blueprint)

    from app.models import db
    db.init_app(app)

    return app
