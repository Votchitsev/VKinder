import datetime
import requests
from pprint import pprint
from config import USER_TOKEN, api_base_url_vk
from iterator import PartnerPhotoIterator


class Partner:
    def __init__(self, birthday, city, sex, token):
        self.token = token
        self.relation = [0, 1, 6]
        self.birthday = birthday
        self.city = city
        self.user_sex = sex

    def count_partner_age(self):
        current_year = datetime.datetime.now()
        birthday = datetime.datetime.strptime(self.birthday, '%Y')
        user_age = current_year.year - birthday.year
        return user_age

    def search_partner_id(self):
        params = {
            'access_token': self.token,
            'count': '1',
            'hometown': self.city,
            'sex': self.determining_the_sex_of_the_partner(),
            'status': self.relation,
            'v': '5.131',
            'age_from': self.count_partner_age() - 3,
            'age_to': self.count_partner_age() + 3,
            'has_photo': '1'
        }

        partner_info = requests.get(api_base_url_vk + 'users.search', params=params)
        partner_id_list = tuple(partner_id['id'] for partner_id in partner_info.json()['response']['items'])
        return partner_id_list

    def get_partner_photo(self, owner_id):
        params = {
            'access_token': self.token,
            'v': '5.131',
            'owner_id': owner_id,
            'album_id': 'profile',
            'extended': '1',
            'count': '1000',
            'photo_sizes': 1
        }
        partner_photo = requests.get(api_base_url_vk + 'photos.get', params=params)
        photo_information = partner_photo.json()['response']['items']
        photo_list = []
        for photo in PartnerPhotoIterator(photo_information):
            photo_list.append(photo)
        photo_list = sorted(photo_list, key=lambda x: x['likes'], reverse=True)
        return photo_list

    def determining_the_sex_of_the_partner(self):
        sex = None
        if self.user_sex == '1':
            sex = '2'
        elif self.user_sex == '2':
            sex = '1'

        return sex
