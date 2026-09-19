from flask import Blueprint

reviews_bp = Blueprint("reviews", __name__)

reviews = [
    {"id": 1, "movie": "Spider-Man", "rating": 5},
    {"id": 2, "movie": "Shrek", "rating": 4},
    {"id": 3, "movie": "Cars", "rating": 5}
]


@reviews_bp.route("/")
def list_reviews():
    return {"data": reviews}


@reviews_bp.route("/<int:review_id>")
def get_review(review_id):
    for review in reviews:
        if review["id"] == review_id:
            return review

    return {"error": "Review not found"}, 404
