import pytest
from partner import Partner
import config


class Test:

    def test_partner_count_age(self):
        partner = Partner('1988', 'калининград', 2, config.USER_TOKEN)
        assert partner.count_partner_age() == 33

    def test_search_partner(self):
        partner = Partner('1988', 'калининград', 2, config.USER_TOKEN)
        i = partner.search_partner_id()[0]
        print(partner.get_partner_photo(i))

