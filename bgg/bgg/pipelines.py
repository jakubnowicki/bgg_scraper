# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from bgg.models import db_connect, create_table, Boardgame, DailyRating


class DBWriter(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        game_id = item['image'].split('/')[2]

        session = self.Session()
        game = session.query(Boardgame).filter_by(id=game_id).first()

        boardgamedb = Boardgame()
        boardgamedb.id = game_id
        boardgamedb.name = item['name']
        boardgamedb.image = item['image']
        boardgamedb.year = item['year']

        dailyratingdb = DailyRating()
        dailyratingdb.game_id = game_id
        dailyratingdb.rank = item['rank']
        dailyratingdb.geek_rating = item['geek_rating']
        dailyratingdb.avg_rating = item['avg_rating']
        dailyratingdb.num_voters = item['num_voters']
        dailyratingdb.timestamp = item['timestamp']

        try:
            if game is None:
                session.add(boardgamedb)
            session.add(dailyratingdb)
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

        return item
