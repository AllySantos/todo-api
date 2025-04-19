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

class UserService:

    def __init__(self):
        pass

    def create_new_user(self, payload):

        action = 'register'
        user_is_valid = self.user_is_valid(payload, action)  # Ensure function is called correctly

        if user_is_valid is False:
            raise Exception("User payload isn't valid")

        user_exists = user_repo.get_user_by_email(payload['email'])

        if user_exists is not None:
            raise UserAlreadyExists()

        # Hash password
        payload = self.set_hashed_password(payload)

        # Create user in database
        user = user_repo.add(user_data=payload)

        # Create token
        token = self.create_new_token(user.id)

        return token


    def login_user(self, payload):

        action = 'login'
        user_is_valid = self.user_is_valid(payload, action)  # Ensure function is called correctly

        if user_is_valid is False:
            raise Exception("User payload isn't valid")

        payload = self.set_hashed_password(payload)

        # Try login user
        logged_user = user_repo.get_user_by_email_and_password(payload['email'], payload['password'])

        if logged_user is None:
            raise UserNotFound()

        token = self.create_new_token(logged_user.id)

        return token

    @staticmethod
    def set_hashed_password(payload):
        original_password = payload['password']
        hashed_password = hash.hash_object(original_password)

        payload['password'] = hashed_password
        return payload

    @staticmethod
    def create_new_token(user_id):
        new_session = token.create_token(user_id)
        created_session = session_repo.add(new_session)
        created_token = created_session['token']

        return {'token': created_token}

    @staticmethod
    def user_is_valid(payload, action):
        required_keys = validate_user_payload[action]

        for key in required_keys:
            if key not in payload:
                return False
        return True



    


