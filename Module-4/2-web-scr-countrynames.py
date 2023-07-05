import requests
from bs4 import BeautifulSoup

# Send a GET request to the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find the table containing the country codes
table = soup.find("table", class_="wikitable sortable")
#print (table)

# Extract the country names
country_names = []
for row in table.find_all("tr"):
    country = row.find_all("a")[1].text.strip()
    country_names.append(country)

# Print the country names
for name in country_names:
    print(name)

# Printing the country names
# for cname in country_names:
#     file = open("Module-4\country_list.txt", "a")
#     file.write(cname+"\n")
#     file.close()

