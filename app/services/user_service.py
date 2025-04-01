from repositories.user_repository import UserRepository
from repositories.session_repository import SessionRepository

from  security import hash, token

user_repo = UserRepository()
session_repo = SessionRepository()

class UserService():

    def __init__(self):
        pass

    def create_new_user(self, object):

        user_is_valid = self.user_is_valid(object)  # Ensure function is called correctly

        if user_is_valid:
            # Hash password
            original_password = object['password']
            hashed_password = hash.hash_object(original_password)

            object['password'] = hashed_password

            # Create user in database
            user_repo.add(user_data=object)

            # Create token
            new_session = token.create_token()
            created_session = session_repo.add(new_session)
            created_token = created_session['token']

            return {'token': created_token}

        return None


    def user_is_valid(self, object):
        required_keys = ['name', 'email', 'password']

        for key in required_keys:
            if key not in object:
                return False
        return True



    


