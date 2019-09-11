from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship
import os

# from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()
basedir = os.path.abspath(os.path.dirname(__file__))


def db_connect():
    return create_engine('sqlite:///' + os.path.join(basedir) +
                         '/boardgames.db',
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
    timestamp = Column(String)

    # boardgame = relationship("Boardgame", back_populates="daily_rating")

    def __repr__(self):
        return self.id
