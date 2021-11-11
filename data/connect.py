import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = sq.create_engine('postgresql://votchitsev:55555@localhost:5432/vkinder')
connection = engine.connect()


Session = sessionmaker(bind=engine)


