from flask import request, Blueprint

from services.user_service import UserService

bp_user = Blueprint('user', __name__)
service = UserService()

@bp_user.route('/', methods=['POST'])
def create_user():
    payload = request.get_json()
    user = service.create_new_user(payload)
    if user is not None:
        return user, 201
    return "error", 400


