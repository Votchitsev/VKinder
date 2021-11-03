import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import config
from user import User

user = User()


class VKBot:
    def __init__(self):
        self.token = config.TOKEN
        self.vk = vk_api.VkApi(token=config.TOKEN)
        self.longpoll = VkLongPoll(self.vk)
        self.user_id = None

    def write_msg(self, user_id, message):
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randrange(10**7)})

    def longpoll_listen(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                self.user_id = event.user_id
                if event.to_me:
                    message = event.message.lower()
                    if message == 'привет':
                        self.write_msg(self.user_id,
                                       'Введите ID пользователя ВКонтакте, для которого хотите найти пару:  ')
                    else:
                        user_id = event.message
                        if not self.check_user_id(user_id):
                            self.write_msg(self.user_id,
                                           'Такого пользователя не существует, или формат ID неверный...')
                        else:
                            user.id = user_id
                            user.get_self_user_info()
                            self.check_user_info()
                            if len(user.birthday) > 4:
                                user.birthday = user.birthday[6:]
                            print(user.sex, user.relations, user.city, user.birthday)

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
            user.city = self.get_more_information()

        if len(user.birthday) < 10:
            self.write_msg(self.user_id, 'Назовите год своего рождения.')
            user.birthday = self.get_more_information()

    def get_more_information(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                self.user_id = event.user_id
                if event.to_me:
                    message = event.message.lower()
                    self.longpoll.listen()
                    return message
