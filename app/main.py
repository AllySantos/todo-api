from models.user import User
from repositories.user_repository import UserRepository

user_data = dict()
user_data['name'] = 'alicia'
user_data['email'] = 'teste@teste.aaacom'
user_data['password'] = '123456'

repository = UserRepository()
user_add = repository.add(user_data)
user = repository.get_user_by_email(user_data['email'])

print(user)