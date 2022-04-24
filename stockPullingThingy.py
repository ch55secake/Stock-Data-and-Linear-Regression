import time
import pandas as pd
from pandas_datareader import data
import json
import requests

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"from_currency": "BTC", "function": "CURRENCY_EXCHANGE_RATE", "to_currency": "USD"}

headers = {
    "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com",
    "X-RapidAPI-Key": "6d48558338msh973a547daf7f4c8p1c460fjsn34222e738ef3"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"time_period": "60", "interval": "5min", "series_type": "close", "function": "RSI", "symbol": "BTC",
               "datatype": "json"}

headers = {
    "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com",
    "X-RapidAPI-Key": "6d48558338msh973a547daf7f4c8p1c460fjsn34222e738ef3"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"time_period": "60", "interval": "5min", "series_type": "close", "function": "OBV", "symbol": "BTC",
               "datatype": "json"}

headers = {
    "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com",
    "X-RapidAPI-Key": "6d48558338msh973a547daf7f4c8p1c460fjsn34222e738ef3"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

querystring = {"function": "CRYPTO_INTRADAY", "symbol": "BTC", "market": "GBP", "interval": "5min"}

headers = {
    "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com",
    "X-RapidAPI-Key": "6d48558338msh973a547daf7f4c8p1c460fjsn34222e738ef3"
}


def collectAllWithKey(key, tSeries):
    out = []
    for v in tSeries.values():
        out.append(v[key])
    return out


intraday = requests.request("GET", url, headers=headers, params=querystring)
newIntraday = intraday.json()
print(newIntraday["Time Series Crypto (5min)"])
high = collectAllWithKey("2. high", newIntraday["Time Series Crypto (5min)"])
low = collectAllWithKey("3. low", newIntraday["Time Series Crypto (5min)"])
for v in low:
    print(v)


def convertingDataToFrame():
    df = pd.read_json(newIntraday.json)
    print(df["high"].appply(pd.Series))
    pd.json_normalize(df)

# def formattingData(dataFrameSDAFADJ, dataFrameSDA):
# print(dataFrameSDA)


# def fetchingData():
#  tickers = ["BTC-USD"]
#  stockDataForAdjClose = data.get_data_yahoo(tickers)
#  stockDataActual = data.get_quote_yahoo(tickers)
# dataFrameSDA = pd.DataFrame(stockDataActual)
# print(stockDataActual)
# dataFrameSDA.to_csv(index=False)
# dataFrameSDAFADJ = pd.DataFrame(stockDataForAdjClose["Adj Close"])
#  print(dataFrameSDAFADJ)
# dataFrameSDAFADJ = dataFrameSDAFADJ.to_csv(index=False)


# class stockData:
# formattingData(dataFrameSDA=True, dataFrameSDAFADJ=True)
# fetchingData()
# pass
