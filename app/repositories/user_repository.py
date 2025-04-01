from database.config import supabase
from utils import parser

class UserRepository:

    def __init__(self):
        self.table_name = 'user'

    def get_user_by_email(self, user_email):
        response = (
            supabase.table(self.table_name)
            .select('*')
            .limit(1)
            .eq('email', user_email)
            .execute()
        )

        user = None
        if len(response.data) > 0:
            response_data = response.data[0]
            user = parser.parse_user(response_data)
        return user


    def get_user_by_email_and_password(self, user_email, user_password):
        response = (
            supabase.table(self.table_name)
            .select('*')
            .limit(1)
            .eq('email', user_email)
            .eq('password', user_password)
            .execute()
        )

        user = None
        if len(response.data) > 0:
            response_data = response.data[0]
            user = parser.parse_user(response_data)
        return user

    def add(self, user_data):

        response = (
            supabase.table(self.table_name)
            .insert(user_data)
            .execute()
        )
        response_data = response.data[0]

        user = parser.parse_user(response_data)
        return user
