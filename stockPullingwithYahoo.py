import time
import pandas as pd
from pandas_datareader import data
import json

# for i in range(0, 55):
tickers = ['TSLA']
stockDataForAdjClose = data.get_data_yahoo(tickers)
stockDataActual = data.get_quote_yahoo(tickers)
dataFrameSDA = pd.DataFrame(stockDataActual["Date"])
dataFrameSDA.to_csv(index=False)
dataFrameSDAFADJ = pd.DataFrame(stockDataForAdjClose)
dataFrameSDAFADJ.to_csv(index=False)


