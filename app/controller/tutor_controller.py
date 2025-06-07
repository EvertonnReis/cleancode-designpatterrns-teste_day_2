from flask import request, jsonify
from app.service.tutor_service import ask_tutor

def handle_ask():
    data = request.get_json()
    question = data.get("question", "")

    if not question.strip():
        return jsonify({"error": "Pergunta inválida"}), 400

    answer = ask_tutor(question)
    return jsonify({"answer": answer})
