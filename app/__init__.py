import os

from dotenv import load_dotenv
from flask import Flask, request

from config import DevConfig
from app.movies.routes import movies_bp
from app.reviews.routes import reviews_bp


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(DevConfig)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    app.register_blueprint(movies_bp, url_prefix="/movies")
    app.register_blueprint(reviews_bp, url_prefix="/reviews")

    @app.before_request
    def log_request():
        print(f"{request.method} {request.path}")

    return app
