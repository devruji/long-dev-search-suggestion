from flask import Blueprint

search_bp = Blueprint(
    "search_bp", __name__, url_prefix="/search", template_folder="templates"
)

from app.search import routes
