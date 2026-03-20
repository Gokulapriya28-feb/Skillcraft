import requests
from bs4 import BeautifulSoup
import csv

url = "https://example.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("div", class_="product")

with open("products.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price", "Rating"])

    for p in products:
        name = p.find("h2").text
        price = p.find("span", class_="price").text
        rating = p.find("span", class_="rating").text

        writer.writerow([name, price, rating])
