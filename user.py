import requests
from configurations.config import api_base_url_vk, TOKEN


class User:
    def __init__(self):
        self.city = None
        self.id = None
        self.birthday = None
        self.sex = None
        self.city = None

    def get_self_user_info(self):
        params = {
            'access_token': TOKEN,
            'user_ids': self.id,
            'v': '5.131',
            'fields': 'sex, bdate, relation, city'
        }

        user_info = requests.get(api_base_url_vk + 'users.get', params=params)

        try:
            self.sex = user_info.json()['response'][0]['sex']
            self.birthday = user_info.json()['response'][0]['bdate']
            self.city = user_info.json()['response'][0]['city']['id']

        except KeyError as key:
            if key == 'city':
                self.city = None
