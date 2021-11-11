import requests

from configurations.config import api_base_url_vk, USER_TOKEN


class City:

    def __init__(self, name: str):
        self.city_name = name.capitalize()
        self.city_id = None

    def get_cities(self):
        params = {
            'access_token': USER_TOKEN,
            'country_id': 1,
            'v': '5.131',
            'need_all': 1,
            'count': 1,
            'q': self.city_name
        }

        response = requests.get(api_base_url_vk + 'database.getCities', params=params)

        if response.json()['response']['count'] == 0:
            return None
        else:
            city_id = response.json()['response']['items'][0]['id']
            return city_id

    def check_city(self):

        result = self.get_cities()

        if result is None:
            return False
        else:
            return True
