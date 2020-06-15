# InstaScrape
This is a scraper for scraping top search results on Instagram

## Usage
```python
from scraper import InstaScraper

#Bot init
scrape_bot = InstaScraper()

#OAuth Authentication
scrape_bot.login('<YOUR USERNAME>', '<YOUR PASSWORD>')

#Get URL
scrape_bot.get_loc("Enter Search Item Here")
```
