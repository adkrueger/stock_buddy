from config import CONFIG_KEY
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as pdr

api_key = CONFIG_KEY

DATE_START = '2020-05-29'
DATE_END = '2020-05-29'
SYMBOL = 'MSFT'

# We use the 'av-daily' DataReader to download data from AlphaVantage
stock = pdr.DataReader(SYMBOL, 'av-daily',
                       start=DATE_START,
                       end=DATE_END,
                       api_key=api_key)

print(stock)
