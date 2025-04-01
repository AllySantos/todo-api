from repositories.user_repository import UserRepository
from repositories.session_repository import SessionRepository

from exceptions.bussiness_exceptions import UserAlreadyExists, UserNotFound

from security import hash, token

user_repo = UserRepository()
session_repo = SessionRepository()

validate_user_payload = {
    'login': ['email', 'password'],
    'register': ['name', 'email', 'password']
}

class UserService():

    def __init__(self):
        pass

    def create_new_user(self, object):

        action = 'register'
        user_is_valid = self.user_is_valid(object, action)  # Ensure function is called correctly

        if user_is_valid is False:
            raise Exception("User payload isn't valid")

        user_exists = user_repo.get_user_by_email(object['email'])

        if user_exists is not None:
            raise UserAlreadyExists()

        # Hash password
        object = self.set_hashed_password(object)

        # Create user in database
        user_repo.add(user_data=object)

        # Create token
        token = self.create_new_token()

        return token


    def login_user(self, object):

        action = 'login'
        user_is_valid = self.user_is_valid(object, action)  # Ensure function is called correctly

        if user_is_valid is False:
            raise Exception("User payload isn't valid")

        object = self.set_hashed_password(object)

        # Try login user
        logged_user = user_repo.get_user_by_email_and_password(object['email'], object['password'])

        if logged_user is None:
            raise UserNotFound()

        token = self.create_new_token()

        return token


    def set_hashed_password(self, object):
        original_password = object['password']
        hashed_password = hash.hash_object(original_password)

        object['password'] = hashed_password
        return object

    def create_new_token(self):
        new_session = token.create_token()
        created_session = session_repo.add(new_session)
        created_token = created_session['token']

        return {'token': created_token}


    def user_is_valid(self, object, action):
        required_keys = validate_user_payload[action]

        for key in required_keys:
            if key not in object:
                return False
        return True



    


