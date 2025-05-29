import json

from aiohttp import InvalidURL
from flask import request, Blueprint, jsonify
from postgrest import APIError

from services.task_service import TaskService
from exceptions.bussiness_exceptions import *

bp_todo = Blueprint('todo', __name__)
service = TaskService()

def __call_service(callable, **kwargs):
    try:
        response = callable(**kwargs)
        return json.dumps(response)

    except TokenExpirated:
        return jsonify({"message": "unauthorized"}), 401

    except UserNotFound as e:
        return jsonify({"error": e.message}), 404

    except UnauthorizedUser:
        return jsonify({"message": "Forbidden"}), 403

    except APIError as e:
        return jsonify({"error": "database connection is not possible", "details": str(e)}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 400



@bp_todo.route('/', methods=['POST'])
def create_task():
    payload = request.get_json()
    token = request.headers.get('Authorization')

    callable = service.create_new_task

    return __call_service(callable, payload=payload, token_value=token)

@bp_todo.route(rule='/<id>', methods=['PUT'])
def update_task(id):
    payload = request.get_json()
    token = request.headers.get('Authorization')

    callable = service.update_task

    return __call_service(callable, payload=payload, task_id=id, token_value=token)

@bp_todo.route('/<id>', methods=['DELETE'])
def delete_task(id):

    token = request.headers.get('Authorization')

    callable = service.delete_task
    return __call_service(callable, task_id=id, token_value=token)

@bp_todo.route('/', methods=['GET'])
def get_tasks():
    token = request.headers.get('Authorization')
    limit = request.args.get('limit')
    page = request.args.get('page')

    if limit is None or page is None:
        return jsonify({"error": 'Please provide limit and page query params'}), 500


    callable = service.get_tasks
    return __call_service(callable, token_value=token, limit=limit, page=page)

