from datetime import datetime, timezone

from repositories.user_repository import UserRepository
from repositories.task_repository import TaskRepository
from repositories.session_repository import SessionRepository

from enums.task_status_enum import TaskStatus

from exceptions.bussiness_exceptions import TokenExpirated, UserNotFound, UnauthorizedUser, TaskNotFound

user_repo = UserRepository()
session_repo = SessionRepository()
task_repo = TaskRepository()

validate_task_payload = {
    'register': ['title', 'description'],
    'update': ['title', 'description']

}

class TaskService:

    def __init__(self):
        pass

    def get_tasks(self, token_value, limit, page):

        limit = int(limit)
        page = int(page)

        # Buscar a existencia do Token
        token = self._get_token(token_value)

        # Buscar o usuário referente aquele token
        user = self._get_user_by_token(token)

        tasks = task_repo.get_tasks_by_user(user.id)

        tasks_payload_data = [task.to_short_dict() for task in tasks]

        # Pagination
        start_index = ((page - 1) * limit)  if page > 1 else 0
        end_index = start_index + limit

        # Validate index according to array limits
        start_index = start_index if len(tasks_payload_data) > start_index else len(tasks_payload_data)
        end_index = end_index if len(tasks_payload_data) > end_index else len(tasks_payload_data)

        paginated_payload = tasks_payload_data[start_index:end_index]


        payload_tasks = {'data': paginated_payload, 'page': page, 'limit': limit, 'total': len(paginated_payload)}
        return payload_tasks


    def delete_task(self, task_id, token_value):
        # Buscar a existencia do Token
        token = self._get_token(token_value)

        # Buscar o usuário referente aquele token
        user = self._get_user_by_token(token)

        # Valida o ID da task e o user dono da task
        task = task_repo.get_task_by_id(task_id)

        if task is None:
            raise TaskNotFound()

        if task.user.id != user.id:
            raise UnauthorizedUser()

        is_task_deleted = task_repo.delete(task.id)

        if not is_task_deleted:
            raise BaseException('Delete was unsuccessful, try again later')

        task.user = user
        task_payload = task.to_dict()
        return task_payload


    def update_task(self, payload, task_id, token_value):
        keys_to_validate = validate_task_payload['update']

        if any(key for key in payload if key not in keys_to_validate) is True:
            raise KeyError(f'Invalid payload, expected for {' or '.join(keys_to_validate)} in payload')

        # Buscar a existencia do Token
        token = self._get_token(token_value)

        # Buscar o usuário referente aquele token
        user = self._get_user_by_token(token)

        # Valida o ID da task e o user dono da task
        task = task_repo.get_task_by_id(task_id)
        if task is None:
            raise TaskNotFound()

        if task.user.id != user.id:
            raise UnauthorizedUser()

        # Atualiza os campos da task
        task = task_repo.update(task_data=payload, task_id=task_id)
        task.user = user

        payload_task = task.to_dict()
        return payload_task

    def create_new_task(self, payload, token_value):

        # Buscar a existencia do Token
        token = self._get_token(token_value)

        # Buscar o usuário referente aquele token
        user = self._get_user_by_token(token)

        # Inserir o usuário junto da task
        payload['user_id'] = user.id

        # Inserir o status padrão
        payload['status'] = TaskStatus.TODO.value
        task = task_repo.add(payload)

        # Atuatilizar o objeto user
        task.user = user

        payload_task = task.to_dict()

        return payload_task


    def _get_user_by_token(self, token):
        user_id = token['user_id']
        user = user_repo.get_user_by_id(user_id)
        if user is None:
            raise UserNotFound()

        return user

    def _get_token(self, token_value):
        token = session_repo.get_session_by_token(token_value)
        is_token_active = self.is_token_active(token)
        if not is_token_active:
            raise TokenExpirated()

        return token

    @staticmethod
    def is_token_active(token):
        current_date = datetime.today().replace(tzinfo=timezone.utc)
        expiration_datetime = datetime.fromisoformat(token['expiration_datetime'])

        return expiration_datetime > current_date


