import json

from flask import request, Blueprint, jsonify

from services.task_service import TaskService
from services.user_service import UserService
from exceptions.bussiness_exceptions import *

bp_todo = Blueprint('todo', __name__)
service = TaskService()

@bp_todo.route('/', methods=['POST'])
def create_task():
    payload = request.get_json()
    token = request.headers.get('Authorization')

    try:
        task = service.create_new_task(payload, token)
        return json.dumps(task)

    except TokenExpirated as e:
        return jsonify({"message": "unauthorized"}), 401

    except UserNotFound as e:
        return jsonify({"error": e.message}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 400
