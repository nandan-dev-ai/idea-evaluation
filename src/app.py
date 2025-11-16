from flask import Flask
from src.routes.similarity import similarity_bp

def create_app():
    """Create and configure Flask app"""
    app = Flask(__name__)
    app.register_blueprint(similarity_bp)
    return app