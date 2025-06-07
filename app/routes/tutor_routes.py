from flask import Blueprint
from app.controller.tutor_controller import handle_ask

tutor_bp = Blueprint("tutor", __name__)
tutor_bp.route("/ask", methods=["POST"])(handle_ask)
