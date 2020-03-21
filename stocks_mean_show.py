import datetime, time
import pandas_datareader
import pandas as pd
import matplotlib.pyplot as plt

from mosc_exch import * #stocks_by_groups

DAYS_IN_YEAR = 365
YEARS_BEFORE_LOAD = 4

def show_stocks(sym):    
    today = datetime.date.today()
    three_years_before = today - datetime.timedelta(DAYS_IN_YEAR*YEARS_BEFORE_LOAD)
    stocks = pandas_datareader.DataReader(sym,'yahoo',three_years_before,today)
    stocks['MA50'] = stocks['Open'].rolling(50).mean()
    stocks['MA100'] = stocks['Open'].rolling(100).mean()
    stocks['MA200'] = stocks['Open'].rolling(200).mean()
    stocks[['Open','MA50','MA100','MA200']].plot(label=sym,figsize=(16,8))
    plt.show()

show_stocks('SBER.ME')
#show_stocks(stocks_by_groups[[group for group in stocks_by_groups][-1]][-1])
