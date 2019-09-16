# BGG scraper

## Development

In order to setup development environment run `./setup_env.sh`

## Runing scrapper

In `bgg` directory run `scrapy crawl bgg_list`. Remember to activate virtual environment (run `source venv/bin/activate`).

## Database

Scraper saves data in PostgreSQL database. Provide credentials as environmental variables:
```
export DB_NAME=bgg_ranking
export DB_PORT=5432
export DB_PASSWORD=password
export DB_SCHEMA=public
export DB_HOST=localhost
```
