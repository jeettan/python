import pandas as pd
import yfinance as yf

print("Helllo world")

msft = yf.Ticker('msft')

stockinfo = msft.info

#for key,value in stockinfo.items():
#	print(key,":",value)

#numshares = msft.info['sharesOutstanding']
#print(numshares)

print(msft.recommendations)
print(msft.splits)

print(type(msft.info))

df = msft.dividends

print(df)

#print(msft.major_holders)

#print(msft.institutional_holders)