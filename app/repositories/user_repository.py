from database.config import supabase
from models.user import User

class UserRepository:

    def __init__(self):
        self.table_name = 'user'

    def add(self, user : User):
        user = user.to_dict()

        response = (
            supabase.table(self.table_name)
            .insert(user)
            .execute()
        )
        response_data = response.data[0]
        return User(response_data['id'], response_data['name'], response_data['email'])

