import requests
from config import api_base_url_vk, TOKEN


class User:
    def __init__(self):
        self.id = None
        self.birthday = None
        self.sex = None
        self.relations = None
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
            self.relations = user_info.json()['response'][0]['relation']
            self.city = user_info.json()['response'][0]['sity']

        except KeyError:
            pass
            # print(f'В вашем профиле не указаны данные {error}')

# relations 0, 1, 6

