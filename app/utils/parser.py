from models.user import User
from models.task import Task
from enums.task_status_enum import TaskStatus

def parse_user(payload):

    user_name = payload['name']
    user_email = payload['email']
    user_password = payload['password']

    user = User(id = None, name=user_name, email=user_email, password=user_password)

    if 'id' in payload:
        user.id = payload['id']

    return user

def parse_task(payload):

    status = TaskStatus(payload['status'])
    user = User(id=payload['id'])

    task = Task(
        title=payload['title'],
        description=payload['description'],
        user=user,
        status=status
    )

    if 'id' in payload:
        task.id = payload['id']

    return task

