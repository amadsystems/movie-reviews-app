from flask import Blueprint, jsonify

movies_bp = Blueprint("movies", __name__)

MOVIES = [
    {"id": 1, "title": "Spider-Man"},
    {"id": 2, "title": "Shrek"},
    {"id": 3, "title": "Cars"},
]


@movies_bp.route("/")
def list_movies():
    return jsonify({"data": MOVIES})


@movies_bp.route("/<int:movie_id>")
def get_movie(movie_id):
    for movie in MOVIES:
        if movie["id"] == movie_id:
            return jsonify(movie)

    return jsonify({"error": "movie not found"}), 404
