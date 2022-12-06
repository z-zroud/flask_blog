import importlib
from flask import Blueprint
import os

bp = Blueprint('api', __name__)


# api_bp = Blueprint('api_bp', __name__,template_folder='../../web', static_folder='../../web', static_url_path='/')
for file in os.listdir(os.path.dirname(__file__)):
    module_name, _ = os.path.splitext(file)
    importlib.import_module(f"app.api.{module_name}")

# from app.api import ping, login, users, posts