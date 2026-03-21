import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the e-commerce site
url = "http://books.toscrape.com/"

# Send request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# List to store data
products = []

# Find all product containers
items = soup.find_all("article", class_="product_pod")

for item in items:
    # Extract product name
    name = item.h3.a["title"]
    
    # Extract price
    price = item.find("p", class_="price_color").text
    
    # Extract rating (stored as class name)
    rating_class = item.find("p")["class"]
    rating = rating_class[1]  # Example: 'Three', 'Five'
    
    # Append to list
    products.append({
        "Name": name,
        "Price": price,
        "Rating": rating
    })

# Convert to DataFrame
df = pd.DataFrame(products)

# Save to CSV
df.to_csv("products.csv", index=False)

print("Data saved to products.csv")