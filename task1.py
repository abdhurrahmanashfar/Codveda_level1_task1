

import requests
from bs4 import BeautifulSoup
import pandas as pd

print("\n Web Scraping")
url = "http://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')
titles = [book.h3.a['title'] for book in books]
prices = [book.find('p', class_='price_color').text for book in books]

scraped_df = pd.DataFrame({'Title': titles, 'Price': prices})
print(scraped_df.head())

scraped_df.to_csv("scraped_books.csv", index=False)
print("Saved CSV → scraped_books.csv")




