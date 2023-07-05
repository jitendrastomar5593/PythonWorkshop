import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Step 1: Define the URL
url = "https://unsplash.com/images/nature/flower"

# Step 2: Send an HTTP GET request and fetch the HTML content
response = requests.get(url)
html_content = response.text

# Step 3: Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Step 4: Find all image tags
image_tags = soup.find_all('img')

# Step 5: Create a directory to save the images
download_directory = 'Module-4\\flower_images'

# Step 6: Download and save the images
for image_tag in image_tags:
    # Get the image URL
    image_url = image_tag.get('src')

    # Handle relative URLs
    if image_url and not image_url.startswith('http'):
        image_url = urljoin(url, image_url)

    # Extract the image filename
    image_filename = os.path.basename(urlparse(image_url).path)

    # Download the image
    image_response = requests.get(image_url)
    with open(os.path.join(download_directory, image_filename), 'wb') as f:
        f.write(image_response.content)

    print(f"Downloaded: {image_filename}")

print("All images downloaded successfully!")
