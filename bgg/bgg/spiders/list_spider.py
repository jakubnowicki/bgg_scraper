import scrapy
from datetime import date


class BggListSpider(scrapy.Spider):
    name = "bgg_list"
    start_urls = [
            'https://boardgamegeek.com/browse/boardgame',
            'https://boardgamegeek.com/browse/boardgame/page/2',
        ]

    def parse(self, response):
        rows = response.css("tr#row_")
        for row in rows:
            rank = row.css("td.collection_rank").css("a::attr(name)").getall()[0]
            image = row.css("td.collection_thumbnail").css("a::attr(href)").getall()[0]
            name = row.css("td.collection_objectname div")[1].css("a::text").getall()[0]
            year = int(row.css("td.collection_objectname div")[1].css("span::text").getall()[0].replace('(', '').replace(')', ''))  # noqa E501
            geek_rating = float(row.css("td.collection_bggrating::text").getall()[0].strip())
            avg_rating = float(row.css("td.collection_bggrating::text").getall()[1].strip())
            num_voters = int(row.css("td.collection_bggrating::text").getall()[2].strip())
            yield {
                'rank': rank,
                'image': image,
                'name': name,
                'year': year,
                'geek_rating': geek_rating,
                'avg_rating': avg_rating,
                'num_voters': num_voters,
                'timestamp': date.today().isoformat(),
            }
