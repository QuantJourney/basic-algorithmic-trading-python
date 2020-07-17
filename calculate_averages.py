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

shortAvgSamples = 9
shortAvgX = np.arange(shortAvgSamples - 1, len(close))
shortAvgY = moving_average(close, shortAvgSamples)

longAvgSamples = 53
longAvgX = np.arange(longAvgSamples - 1, len(close))
longAvgY = moving_average(close, longAvgSamples)

shortAvgX = shortAvgX[longAvgSamples-shortAvgSamples:]
shortAvgY = shortAvgY[longAvgSamples-shortAvgSamples:]

plt.plot(close)
plt.plot(shortAvgX, shortAvgY)
plt.plot(longAvgX, longAvgY)
plt.show()