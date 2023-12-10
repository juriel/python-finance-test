import pandas as pd
import yfinance as yf
import mplfinance as mpl
import datetime
import matplotlib.pyplot as plt

stock = "TSLA"
today = datetime.date.today()
one_year_ago = today - datetime.timedelta(days=365)

start_date = one_year_ago.strftime('%Y-%m-%d')


data = yf.download(stock,start_date)
data.to_excel("data/"+stock+".xlsx")
#data = pd.read_excel("data/"+stock+".xlsx",index_col=0)
print(data)

mpl.plot(data, type="candle", title=stock, style="yahoo", volume=True,mav=(15,30,60))