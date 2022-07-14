from flask import Flask
from app.api import bp as api_bp
from app.plugins import db, migrate
from config import Config
from app.models import *
from app.commands import cmd_bp
from flask_cors import CORS

def create_app(app_config=Config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(app_config)
    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprint(app)
    return app



def register_blueprint(app):
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(cmd_bp)

