from flask import request, Blueprint, jsonify

from services.user_service import UserService
from exceptions.bussiness_exceptions import *

bp_user = Blueprint('user', __name__)
service = UserService()

@bp_user.route('/', methods=['POST'])
def create_user():
    payload = request.get_json()
    try:
        user = service.create_new_user(payload)
        return user
    except UserAlreadyExists as e:
        return jsonify({"error": e.message}), 400

    except Exception as e:
        return str(e), 400



