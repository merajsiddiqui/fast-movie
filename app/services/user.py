from typing import Union, Dict

from app.models import user


def authenticate(login_credentials: user.LoginRequestBody) -> Union[Dict, None]:
    user_detail = {
        'name': 'Meraj Ahmad Siddiqui',
        'email': 'merajsiddiqui@outlook.com',
        'password': 'meraj123'
    }
    if login_credentials.email == user_detail['email'] and login_credentials.password == user_detail['password']:
        return user_detail
    else:
        return None



class User:
    pass
