import requests
from configurations.config import api_base_url_vk


def check_partner_city(partner_id, user_city_id, token):

    params = {
        'access_token': token,
        'fields': 'city',
        'v': '5.131',
        'user_ids': partner_id
    }

    response = requests.get(api_base_url_vk + 'users.get', params=params)

    response = response.json()

    try:
        city = response['response'][0]['city']['id']

        if city == user_city_id:
            return True
        else:
            return False
    except KeyError:
        return False
