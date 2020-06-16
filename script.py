from scraper import InstaScraper
import pandas as pd

#Change required Path here
CSV_PATH = "./insta.csv"

#Bot init
scrape_bot = InstaScraper()

#OAuth Authentication
scrape_bot.login('<USERNAME>', '<PASSWORD>')

#Read CSV
scrape_csv = pd.read_csv(CSV_PATH)

#Scraping Loop
locations = scrape_csv['Apartment Name'] + ' ' + scrape_csv['City']
links = []
for location in locations:
    try:
        scrape_bot.search(location)
        links.append(scrape_bot.get_locs())
    except:
        links.append("NOT FOUND")

#Save Results
scrape_csv['Links']=links
scrape_csv.to_csv('insta_locs.csv', index=False)
scrape_bot.end()