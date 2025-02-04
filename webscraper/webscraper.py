import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for successful response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all URLs from anchor tags <a href="...">
        links = soup.find_all('a', href=True)
        urls = [urljoin(url, link['href']) for link in links]

        # Extract all image sources from <img src="...">
        images = soup.find_all('img', src=True)
        image_sources = [urljoin(url, img['src']) for img in images]

        return urls, image_sources

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}", []
