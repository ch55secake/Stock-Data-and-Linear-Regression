import time
import pandas as pd
import requests


def isSupport(df, i):
    support = df['Low'][i] < df['Low'][i - 1] and df['Low'][i] < df['Low'][i + 1] and df['Low'][i + 1] < df['Low'][
        i + 2] and df['Low'][i - 1] < df['Low'][i - 2]
    return support


def isResistance(df, i):
    resistance = df['High'][i] > df['High'][i - 1] and df['High'][i] > df['High'][i + 1] and df['High'][i + 1] > \
                 df['High'][i + 2] and df['High'][i - 1] > df['High'][i - 2]
    return resistance


def checkOnRsi(df2):
    if df2.iloc[:, 0].gt(70, 90).all():
        print(
            "Values of 70 or above indicate that an asset is becoming overbought and may be primed for a trend reversal or experience correction in the Bitcoin price.")
        return True
    elif df2.iloc[:, 0].lt(0, 35).all():
        print("An RSI reading of 30 or below indicates an oversold or undervalued condition.")
    return False


def collectAllWithKey(key, tSeries):
    out = []
    for v in tSeries.values():
        out.append(v[key])
    return out


# url = "https://alpha-vantage.p.rapidapi.com/query"
#
# querystring = {"from_currency": "BTC", "function": "CURRENCY_EXCHANGE_RATE", "to_currency": "USD"}
#
# headers = {
#     "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com",
#     "X-RapidAPI-Key": ""
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"time_period": "60", "interval": "5min", "series_type": "close", "function": "RSI", "symbol": "BTCGBP",
               "datatype": "json"}

headers = {
    "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com",
    "X-RapidAPI-Key": ""
}

RSI = requests.request("GET", url, headers=headers, params=querystring)
newRSI = RSI.json()
print(newRSI["Technical Analysis: RSI"])
rsiOUT = collectAllWithKey("RSI", newRSI["Technical Analysis: RSI"])
df2 = pd.DataFrame({
    "RSI": rsiOUT,
})


for i in range(0, len(df2)):
    df2["RSI"] = pd.to_numeric(df2["RSI"], errors='coerce').fillna(0, downcast='infer')
    print(f"Row {i}: {df2['RSI'][i]} Check on : {checkOnRsi(df2)}")

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"interval": "5min", "function": "MACD", "symbol": "BTCGBP",
               "datatype": "json", "series_type": "open", "time_period": "60"}

headers = {
    "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com",
    "X-RapidAPI-Key": ""
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

querystring = {"function": "CRYPTO_INTRADAY", "symbol": "BTC", "market": "GBP", "interval": "5min"}

headers = {
    "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com",
    "X-RapidAPI-Key": ""
}

intraday = requests.request("GET", url, headers=headers, params=querystring)
newIntraday = intraday.json()
print(newIntraday["Time Series Crypto (5min)"])
high = collectAllWithKey("2. high", newIntraday["Time Series Crypto (5min)"])
low = collectAllWithKey("3. low", newIntraday["Time Series Crypto (5min)"])
df = pd.DataFrame({
    "High": high,
    "Low": low,
})

for i in range(2, len(df)):
    print(f"Row {i}: {df['High'][i]} {df['Low'][i]} Is Support: {isSupport(df, i)} Is Resistant: {isResistance(df, i)}")
