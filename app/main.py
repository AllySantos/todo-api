from security import token, hash
from models.user import User
from repositories.user_repository import UserRepository
from repositories.session_repository import SessionRepository

user_data = dict()
user_data['name'] = 'alicia'
user_data['email'] = 'teste@teste.aaacom'
user_data['password'] = '123456'


repository = SessionRepository()
session = token.create_token()
created_session = repository.add(session)
token = repository.get_session_by_token(session['token'])

print(created_session)
print(token)
