from flask import Flask
from app.routes.tutor_routes import tutor_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(tutor_bp, url_prefix="/api/tutor")
    return app
