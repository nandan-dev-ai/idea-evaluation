from flask import Blueprint, request, jsonify
from src.services.similarity_service import SimilarityService

similarity_bp = Blueprint('similarity', __name__)
service = SimilarityService()

@similarity_bp.route("/check", methods=["POST"])
def check_similarity():
    """Endpoint to check idea similarity"""
    try:
        data = request.get_json()
        result = service.check_similarity(
            data.get("newIdea"),
            data.get("existingIdeas")
        )
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500