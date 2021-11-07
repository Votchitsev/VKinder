import requests

from configurations.config import api_base_url_vk


def check_token(token):
    params = {
        'access_token': token,
        'user_ids': 1,
        'v': '5.131',
    }

    response = requests.get(api_base_url_vk + 'users.get', params=params)
    response = response.json()
    determination_error_or_not = list(response)

    if determination_error_or_not[0] == 'error':
        print(response['error']['error_msg'])
        return False
    elif determination_error_or_not[0] == 'response':
        return True
