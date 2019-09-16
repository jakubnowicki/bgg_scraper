from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def crawl(spider_name):
    process = CrawlerProcess(get_project_settings())

    process.crawl(spider_name)
    process.start()


if __name__ == "__main__":
    crawl("bgg_list")
