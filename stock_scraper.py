import requests
from bs4 import BeautifulSoup


def scrape_url(ticker):
    yahooURL = 'https://finance.yahoo.com/quote/' + ticker + '/analysis?p=' + ticker
    guruURL = 'https://www.gurufocus.com/stock/' + ticker + '/summary'
    mbURL = 'https://www.marketbeat.com/stocks/' + ticker + '/'
    try:
        yahooResp = requests.get(yahooURL)
        yahooResp.raise_for_status()
        guruResp = requests.get(guruURL)
        guruResp.raise_for_status()
        mbResp = requests.get(mbURL)
        mbResp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        print('\nPlease refresh the page and try again')
        exit()

    yahooSoup = BeautifulSoup(yahooResp.text, 'html.parser')
    guruSoup = BeautifulSoup(guruResp.text, 'html.parser')
    mbSoup = BeautifulSoup(mbResp.text, 'html.parser')

    # growth in last 5 years and next 5 years
    growth_last5 = yahooSoup.find_all('tr')[-1].find_all('td')[1]
    growth_next5 = yahooSoup.find_all('tr')[-2].find_all('td')[1]
    # return on invested capital
    roic = guruSoup.find_all(class_='bar-divider')
    roic = [div.text[6:-1] for div in roic if 'ROIC' in div.text][0]
    # debt to equity ratio
    dte = mbSoup.find_all(class_='price-data')
    quick = dte
    #payout = dte
    dte = [div.text[20:] for div in dte if 'Debt-to-Equity' in div.text][0]
    # quick ratio
    quick = [div.text[11:] for div in quick if 'Quick' in div.text][0]
    # payout ratio - doesn't exist?
    #payout = [div.text[12:] for div in payout if 'Payout' in div.text][0]

    print(growth_last5.text)
    print(growth_next5.text)
    print(roic)
    print(dte)
    print(quick)


scrape_url('MSFT')
