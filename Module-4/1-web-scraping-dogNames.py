import requests
from bs4 import BeautifulSoup

# Send a GET request to the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_dog_breeds"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find the table containing the dog breeds
table = soup.find("div", class_="div-col")
#print (table)

# Extract the titles of the dog breeds
titles = []
for row in table.find_all("li"):
    breed = row.find("a").text.strip()
    titles.append(breed)

# Print the titles
for title in titles:
    print(title)
