import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://books.toscrape.com/"

# Send request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:

    # Read the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book containers
    books = soup.find_all("article", class_="product_pod")

    print("Book Details")
    print("-" * 50)

    # Extract book title and price
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text

        print("Title :", title)
        print("Price :", price)
        print("-" * 50)

else:
    print("Failed to access the website")