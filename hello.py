import pandas as pd
import yfinance as yf
import mplfinance as mpl

# Get the data for the stock AAPL

data = yf.download('AAPL','2016-01-01')

# Import the plotting library
import matplotlib.pyplot as plt

mpl.plot(data, style="yahoo")