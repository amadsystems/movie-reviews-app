from flask import Blueprint, jsonify

reviews_bp = Blueprint("reviews", __name__)

REVIEWS = [
    {"id": 1, "movie_id": 1, "rating": 5},
    {"id": 2, "movie_id": 2, "rating": 4},
]


@reviews_bp.route("/")
def list_reviews():
    return jsonify({"data": REVIEWS})


@reviews_bp.route("/<int:review_id>")
def get_review(review_id):
    for review in REVIEWS:
        if review["id"] == review_id:
            return jsonify(review)

    return jsonify({"error": "review not found"}), 404
