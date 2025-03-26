from models.user import User

def parse_user(object):


    user_name = object['name']
    user_email = object['email']
    user_password = object['password']

    user = User(id = None, name=user_name, email=user_email, password=user_password)

    if 'id' in object:
        user.id = object['id']

    return user