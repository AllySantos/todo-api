from flask import request, Blueprint, jsonify

from services.user_service import UserService
from exceptions.bussiness_exceptions import *

bp_login = Blueprint('login', __name__)
service = UserService()

@bp_login.route('/', methods=['POST'])
def login_user():
    payload = request.get_json()
    try:
        user = service.login_user(payload)
        return user
    except UserNotFound as e:
        return jsonify({"error": e.message}), 404

    except Exception as e:
        return str(e), 400



