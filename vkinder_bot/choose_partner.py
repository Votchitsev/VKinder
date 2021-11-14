from vkinder_bot.check_city import check_partner_city
from data.check import check


def choose_partner(partner_list: list, user_id, city, token):

    for partner in partner_list:

        if check(user_id, partner) and check_partner_city(partner, city, token):
            return partner
        else:
            pass
