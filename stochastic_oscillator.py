import yfinance as yf
import matplotlib.pyplot as plt

def stoc(ticker,duration='1Y',field='Close',period=14):
  print("Details:",ticker,duration,field,period)
  msft=yf.Ticker(ticker)
  hist=msft.history(period=duration)
  dates=hist.index.tolist()
  dates=(dates[0:len(dates)-period])
  _dates=[]
  for i in dates:
    _dates.append(i.to_pydatetime().date())
    
  close=[]
  high=[]
  low=[]
  stoc=[]

  for i in hist[field]:
    close.append(i)

  for i in hist['High']:
    high.append(i)

  for i in hist['Low']:
    low.append(i)

  for i in range(period,(len(hist))):
    hperiod=max(high[i-period:i])
    lperiod=min(low[i-period:i])
    stoc.append(100*(close[i-1]-lperiod)/(hperiod-lperiod))
  plt.plot(_dates,stoc)
  plt.plot(_dates,close[period:])
