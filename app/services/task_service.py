from datetime import datetime, timezone

from repositories.user_repository import UserRepository
from repositories.task_repository import TaskRepository
from repositories.session_repository import SessionRepository

from enums.task_status_enum import TaskStatus

from exceptions.bussiness_exceptions import TokenExpirated, UserNotFound

user_repo = UserRepository()
session_repo = SessionRepository()
task_repo = TaskRepository()

validate_task_payload = {
    'register': ['title', 'description']
}

class TaskService:

    def __init__(self):
        pass

    def create_new_task(self, payload, token_value):

        action = 'register'

        # Buscar a existencia do Token
        token = session_repo.get_session_by_token(token_value)
        is_token_active = self.is_token_active(token)

        if not is_token_active:
            raise TokenExpirated()

        # Buscar o usuário referente aquele token
        user_id = token['user_id']
        user = user_repo.get_user_by_id(user_id)

        if user is None:
            raise UserNotFound()

        # Inserir o usuário junto da task
        payload['user_id'] = user_id

        # Inserir o status padrão
        payload['status'] = TaskStatus.TODO.value
        task = task_repo.add(payload)
        task.user = user

        payload_task = task.to_dict()

        return payload_task


    @staticmethod
    def is_token_active(token):
        current_date = datetime.today().replace(tzinfo=timezone.utc)
        expiration_datetime = datetime.fromisoformat(token['expiration_datetime'])

        return expiration_datetime > current_date


