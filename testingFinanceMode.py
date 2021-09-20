import pandas as pd
import pandas_ta
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from pandas_datareader import data
import matplotlib.pyplot as plt


dataFrame = pd.read_csv("TSLA.csv")
dataFrame.set_index(pd.DatetimeIndex(dataFrame["Date"]), inplace=True)
dataFrame = dataFrame[["Adj Close"]]


dataFrame.ta.ema(close="adj close", length=10, append=True)
dataFrame = dataFrame.iloc[10:]


X_train, X_test, y_train, y_test = train_test_split(dataFrame[['Adj Close']], dataFrame[['EMA_10']], test_size=.2)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = (model.predict(y_test))
x_pred = (model.predict(X_test))


print(X_test.describe())

print(X_train.describe())

print(y_pred)
print(x_pred)

# Printout relevant metrics
print("Model Coefficients:", model.coef_)
print("Model intercept:", model.intercept_)
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Coefficient of Determination:", r2_score(y_test, y_pred))

# xAxis = [100, 200, 300, 400, 500, 600, 700]
# yAxis = [100, 200, 300, 400, 500, 600, 700]
# plt.plot(xAxis, yAxis)
# plt.title("Test")
# plt.show()




