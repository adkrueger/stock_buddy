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

    soup = BeautifulSoup(response.text, 'html.parser')
    growth_last5 = soup.find_all('tr')[-1].find_all('td')[1]
    print(growth_last5.text)


scrape_url('https://finance.yahoo.com/quote/MSFT/analysis?p=MSFT')
