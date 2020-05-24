import requests
from bs4 import BeautifulSoup


def scrape_url(ticker):
    yahooURL = 'https://finance.yahoo.com/quote/' + ticker + '/analysis?p=' + ticker

    try:
        yahooResp = requests.get(yahooURL)
        yahooResp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        print('\nPlease refresh the page and try again')
        exit()

    soup = BeautifulSoup(yahooResp.text, 'html.parser')
    growth_last5 = soup.find_all('tr')[-1].find_all('td')[1]
    growth_next5 = soup.find_all('tr')[-2].find_all('td')[1]
    print(growth_last5.text)
    print(growth_next5.text)


scrape_url('MSFT')
