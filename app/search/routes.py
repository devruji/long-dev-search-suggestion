from flask import jsonify, render_template, abort, request
from jinja2 import TemplateNotFound
from sqlalchemy import desc

from app.search import search_bp
from app.models.user import Users


@search_bp.route("/", methods=["GET"])
def search():
    try:
        name = request.args.get("name")

        if name:
            users = (
                Users.query.filter(Users.name.ilike(f"{name}%"))
                .order_by(desc(Users.name))
                .limit(5)
                .all()
            )
            # user = Users.query.filter_by(name="David Curtis").first()
            print(f"INFO: Query -> [{name}]", f"INFO: Found -> {users}", sep="\n")
            print("-" * 100)
            return jsonify({"name": [u.name for u in users]})
        return render_template("search.html")
    except TemplateNotFound:
        abort(404)
