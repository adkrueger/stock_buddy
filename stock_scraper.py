import requests
from bs4 import BeautifulSoup


def scrape_url(url):
    response = None
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        print('\nPlease refresh the page and try again')
        exit()
