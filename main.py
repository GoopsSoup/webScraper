import requests
import csv
from bs4 import BeautifulSoup as bs 


url = "https://www.scrapethissite.com/pages/forms/."
url2 = "https://webscraper.io/test-sites/e-commerce/more"
req = requests.get(url)
req2 = requests.get(url2)

soup = bs(req.text, "html.parser")
soup2 = bs(req2.text, "html.parser")
quote = soup.find_all("tr", class_="team")
quote = soup2.find_all("tr", class_="team")


filled = []
for i in quote:
    name = i.find("td", class_="name").get_text(strip=True)
    year = i.find("td", class_="year").get_text(strip=True)
    win = i.find("td", class_="wins").get_text(strip=True)
    lose = i.find("td", class_="losses").get_text(strip=True)
    filled.append((name, year, win, lose))

with open("web.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Team", "Year", "Win", "Lose"])

    for name, year, win, lose in filled:
        writer.writerow([name, year, win, lose])