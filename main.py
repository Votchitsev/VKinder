from vkinder_bot.vk_bot import VKBot
from data.tables import create_database_table

if __name__ == '__main__':

    create_database_table()

    bot = VKBot()

    bot.longpoll_listen()
