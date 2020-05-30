import requests
from bs4 import BeautifulSoup


def scrape_url(ticker):
    yahooURL = 'https://finance.yahoo.com/quote/' + ticker + '/analysis?p=' + ticker
    guruURL = 'https://www.gurufocus.com/stock/' + ticker + '/summary'
    try:
        yahooResp = requests.get(yahooURL)
        yahooResp.raise_for_status()
        guruResp = requests.get(guruURL)
        guruResp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        print('\nPlease refresh the page and try again')
        exit()

    yahooSoup = BeautifulSoup(yahooResp.text, 'html.parser')
    growth_last5 = yahooSoup.find_all('tr')[-1].find_all('td')[1]
    growth_next5 = yahooSoup.find_all('tr')[-2].find_all('td')[1]
    print(growth_last5.text)
    print(growth_next5.text)


scrape_url('MSFT')
