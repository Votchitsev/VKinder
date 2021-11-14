import sqlalchemy as sq

from data.connect import Base, Session, engine


class PartnersBase(Base):

    __tablename__ = 'partners'

    id = sq.Column(sq.Integer, primary_key=True)
    searcher_id = sq.Column(sq.String, nullable=False)
    partner_id = sq.Column(sq.Integer, nullable=False)
    partner_first_name = sq.Column(sq.String)
    partner_last_name = sq.Column(sq.String)


def create_database_table():
    session = Session()
    Base.metadata.create_all(engine)
    session.commit()
