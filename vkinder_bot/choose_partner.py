from vkinder_bot.check_city import check_partner_city
from data.check import check


def choose_partner(partner_list: list, user):
    for partner in partner_list:
        if check(user.id, partner) and check_partner_city(partner, user.city):
            return partner
        else:
            pass
