import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, mapper

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
