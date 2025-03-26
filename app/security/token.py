import datetime
import random
import string
from datetime import datetime
import datetime as dt

token_lenght = 30
expiration_minutes = 30


def create_token():
    token = ''.join(random.choices(string.ascii_letters, k=token_lenght))
    expiration_datetime = get_expiration_datetime()

    token_dict = dict()
    token_dict['token'] = token
    token_dict['expiration_date'] = expiration_datetime
    return token_dict


def get_expiration_datetime():
    current_date = datetime.today()
    minutes = dt.timedelta(minutes=expiration_minutes)
    expiration_date = current_date + minutes
    expiration_date = expiration_date.isoformat()
    return expiration_date


