from data.connect import Session
from data.tables import PartnersBase


def check(searcher_id, partner_id):

    session = Session()

    partners = session.query(PartnersBase).filter(
        PartnersBase.searcher_id == searcher_id,
        PartnersBase.partner_id == partner_id).all()

    partners = [partner for partner in partners]
    if len(partners) == 0:
        return True
    else:
        return False
