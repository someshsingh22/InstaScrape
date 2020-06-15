from scraper import InstaScraper
import pandas as pd

#Change required Path here
CSV_PATH = "./INSTA.csv"

scrape_bot = InstaScraper()

#OAuth Authentication
scrape_bot.login('<YOUR USERNAME>', '<YOUR PASSWORD>')

#Read CSV
scrape_csv = pd.read_csv(CSV_PATH)

#Scraping Loop
locations = scrape_csv['Apartment Name'] + ' ' + scrape_csv['City']
links = []
for location in locations:
    try:
        links.append(scrape_bot.get_loc(location))
    except:
        links.append("NOT FOUND")

#Save Results
scrape_csv['Links']=links
scrape_csv.to_csv('insta_locs.csv', index=False)