from models.user import User
from repositories.user_repository import UserRepository

alicia = User(name='Alicia', email='teste@teste.com')

repository = UserRepository()
user_add = repository.add(alicia)
print(user_add)