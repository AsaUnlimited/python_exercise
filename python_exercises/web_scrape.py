# "https://www.goodreads.com/siteindex.quote.xml"
import time
import requests
from bs4 import BeautifulSoup
from csv import writer
while True:
    url = ("https://www.rithmschool.com/blog")

    response = requests.get(url)
    # print(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article")
    # print(articles)

    with open("scrape_data.csv", mode='w') as scrape_data_write:
        csv_write = writer(scrape_data_write)
        csv_write.writerow([f"Title \t\t\t" "Date \t\t" "Link"])
        for article in articles:
            a_link = article.find("a")
            title = a_link.get_text()
            link = a_link["href"]
            date = article.find("time")["datetime"]
            csv_write.writerow([title, date, link])
    time.sleep(20)