from flask import jsonify, render_template, abort, request
from jinja2 import TemplateNotFound
from sqlalchemy import desc

from app.search import search_bp
from app.models.user import Users


@search_bp.route("/", methods=["GET"])
def search():
    try:
        terms = request.args.get("searchTerm")

        if terms:
            keywords = (
                Users.query.filter(Users.keyword.ilike(f"{terms}%"))
                .order_by(desc(Users.score))
                .limit(5)
                .all()
            )

            # ?: Log search results
            print(f"INFO: Query -> [{terms}]")
            for idx, _ in enumerate(keywords):
                print(
                    f"INFO: Result [{idx+1}] -> keyword: {_.keyword} | score: {_.score}"
                )
            print("-" * 100)

            return jsonify({"suggestions": [k.keyword for k in keywords]})

        return render_template("search.html")

    except TemplateNotFound:
        abort(404)
