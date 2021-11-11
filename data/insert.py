from data.connect import Session
from data.tables import PartnersBase


def insert(searcher_id, partner_id, partner_first_name, partner_last_name):

    session = Session()

    record = PartnersBase(
        searcher_id=searcher_id,
        partner_id=partner_id,
        partner_first_name=partner_first_name,
        partner_last_name=partner_last_name
    )

    session.add(record)
    session.commit()
