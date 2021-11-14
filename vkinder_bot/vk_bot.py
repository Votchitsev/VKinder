import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from vkinder_bot.choose_partner import choose_partner
from configurations import config
from vkinder_bot.user import User
from vkinder_bot.partner.partner import Partner
from vkinder_bot.cities import City
from configurations.check_token import check_token
import requests
from configurations.config import api_base_url_vk
from data.insert import insert
import datetime

user = User()


class VKBot:

    def __init__(self):
        self.token = config.access_token
        self.vk = vk_api.VkApi(token=config.TOKEN)
        self.longpoll = VkLongPoll(self.vk)
        self.user_id = None

    def write_msg(self, user_id, message, attachment=None):
        self.vk.method('messages.send', {'user_id': user_id, 'message': message,
                                         'attachment': attachment, 'random_id': random.randrange(10 ** 7)})

    def longpoll_listen(self):

        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                self.user_id = event.user_id
                if event.to_me:
                    message = event.message

                    if not check_token(config.access_token):
                        self.token = self.insert_new_token()

                    if message == 'Начать':
                        self.write_msg(self.user_id,
                                       'Введите  ID пользователя ВКонтакте, для которого хотите найти пару:  ')
                    else:
                        user_id = event.message
                        if not self.check_user_id(user_id):
                            self.write_msg(self.user_id,
                                           'Такого пользователя не существует, или формат ID неверный...')
                        else:

                            self.retrieving_user_information(user_id)

                            partner = Partner(user.birthday, user.city, user.sex, self.token)
                            partner_list = partner.search_partner_id()

                            partner_id = choose_partner(partner_list, user.id, user.city, self.token)

                            partner_photos = partner.get_partner_photo(partner_id)
                            self.sending_found_partners(partner_id, partner_photos)

                            partner_first_name, partner_last_name = self.get_partner_name(partner_id)
                            insert(user.id, partner_id, partner_first_name, partner_last_name)

                            user.city = None
                            user.birthday = None

    def check_user_id(self, user_id):
        try:
            response = self.vk.method('users.get', {'user_ids': user_id})
            if 'deactivated' in response[0]:
                return False
            return user_id
        except vk_api.exceptions.ApiError:
            return False

    def check_user_info(self):
        if user.city is None:
            self.write_msg(self.user_id, 'Назовите город, в котором вы проживаете.')

            while True:
                user_city_tittle = self.get_more_information()
                city = City(user_city_tittle, self.token)
                if city.check_city():
                    user.city = city.get_cities()
                    break
                else:
                    self.write_msg(self.user_id, 'Такого города не существует! Введите заново.')

        if user.birthday is None or len(user.birthday) < 10:
            self.write_msg(self.user_id, 'Назовите год своего рождения.')

            while True:

                birthday = self.get_more_information()

                if birthday.isdigit():
                    if len(birthday) == 4 and (datetime.datetime.now().year - 18) > int(birthday) > 1940:
                        user.birthday = birthday
                        break
                    else:
                        self.write_msg(self.user_id, 'Неверный формат даты, либо вы слишком малы/стары для этого! '
                                                     'Введите заново.')
                else:
                    self.write_msg(self.user_id, 'Дата должна состоять из одних цифр')

        else:
            user.birthday = user.birthday[6:]

    def get_more_information(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                self.user_id = event.user_id
                if event.to_me:
                    message = event.message.lower()
                    self.longpoll.listen()
                    return message

    def sending_found_partners(self, partner_id, partner_photos):
        link_to_partner_page = f"https://vk.com/id{partner_id}"
        for photo in partner_photos:
            self.write_msg(self.user_id,
                           message=link_to_partner_page,
                           attachment=f'photo{partner_id}_{photo["id"]}')

    def insert_new_token(self):

        while not check_token(self.token):
            self.write_msg(self.user_id, 'Введите актуальный ТОКЕН: ')
            new_token = self.get_more_information()
            self.token = new_token
            check_token(config.access_token)

        return self.token

    def retrieving_user_information(self, user_id):
        user.id = user_id
        user.get_self_user_info(self.token)
        self.check_user_info()

    def get_partner_name(self, partner_id):

        params = {
            'access_token': self.token,
            'v': '5.131',
            'user_ids': partner_id,
        }

        response = requests.get(api_base_url_vk + 'users.get', params=params)
        response = response.json()

        first_name = response['response'][0]['first_name']
        last_name = response['response'][0]['last_name']

        return first_name, last_name
