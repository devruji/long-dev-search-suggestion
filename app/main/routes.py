from flask import jsonify, request

from app.main import main_bp
from app.models.user import Users


@main_bp.route("/", methods=["GET"])
def index():
    value = request.args.get("valname")
    if value:
        url = Users.query.filter_by(name=value).first().website[1:-1]
        return jsonify({"urlLink": url})

    return "Hello, World!", 200


@main_bp.route("healthcheck", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200
