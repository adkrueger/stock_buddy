from config import CONFIG_KEY
import requests
import time

'''
Past 5 Year Earnings Growth Rate (can be found on Yahoo! Finance under the Analysis tab) anything above 10% is good.
Return on Invested Capital (ROIC) (Can be found on Guru Focus) anything above 10% is good.
Debt to Equity Ratio (Can be found on Marketbeat or Macrotrends) anything equal to or below 1 is good.
Quick Ratio (Can be found on Marketbeat or Macrotrends) anything equal to or above 1 is good.
Payout Ratio (Can be found on Marketbeat) anything below 35% is good.
Projected 5 Year Earnings Growth Rate (Can be found on Yahoo! Finance under the Analysis tab) anything above 10% is good.


Typical Valuation Methods

Earnings Yield - 6% is an acceptable rate of return, 10% is fantastic
PEG Ratio - 1 or below is acceptable, 0.5 is fantastic
Discount to Fair Value using DCF on the Projected 5 Year Earnings Growth Rate with a discount rate of 10% - Any discount is acceptable, a discount of 50% or below is fantastic and a strong buying signal
EV/EVITBA - 10 or below is acceptable, 7.5 or below is fantastic
Potential 1 Year Gain Using Consenus Analyst Estimates - 20% is acceptable, 30% is fantastic
'''


API_KEY = CONFIG_KEY

TODAY = time.strftime('%Y-%m-%d', time.gmtime())
SYMBOL = 'MSFT'
INTRA_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + \
    SYMBOL + '&interval=5min&apikey=' + API_KEY
QUOTE_URL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + \
    SYMBOL + '&apikey=' + API_KEY

try:
    intra_resp = requests.get(INTRA_URL)
    intra_resp.raise_for_status()
    quote_resp = requests.get(QUOTE_URL)
    quote_resp.raise_for_status()
except requests.exceptions.RequestException as e:
    print(e)
    print('\nPlease refresh the page and try again')
    exit()

print(intra_resp.text)
print(quote_resp.json)
