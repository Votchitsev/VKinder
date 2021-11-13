from partner.partner import Partner
from configurations import config
import cyties


class Test:

    def test_partner_count_age(self):
        partner = Partner('1988', 'калининград', 2, config.USER_TOKEN)
        assert partner.count_partner_age() == 33

    def test_search_partner(self):
        partner = Partner('1988', 'калининград', 1, config.USER_TOKEN)
        i = partner.search_partner_id()
        partner.get_partner_photo(i)

    def test_city(self):
        city = cyties.City('калининград')
        print(city.get_cities())

