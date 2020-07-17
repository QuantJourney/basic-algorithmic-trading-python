import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

stockData = yf.Ticker("IBM")

# Get stock info
data = stockData.history(period="5y")

# Get close price
close = data['Close'].to_numpy()

def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

shortAvgSamples = 10
shortAvgX = np.arange(shortAvgSamples - 1, len(close))
shortAvgY = moving_average(close, shortAvgSamples)

longAvgSamples = 80
longAvgX = np.arange(longAvgSamples - 1, len(close))
longAvgY = moving_average(close, longAvgSamples)

shortAvgX = shortAvgX[longAvgSamples-shortAvgSamples:]
shortAvgY = shortAvgY[longAvgSamples-shortAvgSamples:]

# Find buy/sell points
diff = longAvgY - shortAvgY
buys = []
sells = []

for d in np.arange(len(diff)):
    if (diff[d] >= 0 and diff[d-1] <= 0):
        sells.append(d + longAvgSamples)
    if (diff[d] <= 0 and diff[d-1] >= 0):
        buys.append(d + longAvgSamples)

if (len(buys) > len(sells)):
    buys.pop()

total = np.sum(close[sells] - close[buys])
print('Profits:', total)
print('Buy & hold:', close[-1] - close[0])

plt.plot(close)
plt.scatter(buys, close[buys], c='green')
plt.scatter(sells, close[sells], c='red')
plt.show()