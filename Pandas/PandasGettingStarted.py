import pandas_datareader as web
df=web.DataReader('AAPL','yahoo','2016/1/1','2017/1/1')
print(df.head())
