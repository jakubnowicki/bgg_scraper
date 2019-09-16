from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, create_engine
from sqlalchemy.orm import relationship
import os
from datetime import date


DeclarativeBase = declarative_base()
basedir = os.path.abspath(os.path.dirname(__file__))
postgres_uri = f"postgresql+psycopg2://{os.environ['DB_USER']}:" \
               f"{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:" \
               f"{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"


def db_connect():
    return create_engine(postgres_uri,
                         echo=True)


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Boardgame(DeclarativeBase):
    __tablename__ = 'boardgames'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String)
    year = Column(Integer)

    daily_ratings = relationship("DailyRating", backref="boardgame")

    def __repr__(self):
        return self.name


class DailyRating(DeclarativeBase):
    __tablename__ = "daily_rating"

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('boardgames.id'))
    rank = Column(Integer)
    geek_rating = Column(Float)
    avg_rating = Column(Float)
    num_voters = Column(Integer)
    timestamp = Column(Date, default=date.today())

    def __repr__(self):
        return self.id
