from database.config import supabase
from models.user import User
import random

class UserRepository:

    def __init__(self):
        self.table_name = 'user'

    def add(self, user : User):
        user = user.to_dict()
        user['id'] = random.randint(0,10)
        response = (
            supabase.table(self.table_name)
            .insert(user, default_to_null=True)
            .execute()
        )
        print(response)