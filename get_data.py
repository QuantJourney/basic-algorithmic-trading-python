import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

stockData = yf.Ticker("IBM")

# Get stock info
data = stockData.history(period="5y")

# Get close price
close = data['Close'].to_numpy()

plt.plot(close)
plt.show()