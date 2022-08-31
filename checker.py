import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime,timedelta


budget = input("Input your Budget:-  ")
ticker = input("Give the Ticker:-  ")
stock = yf.Ticker(ticker)
price = stock.info["currentPrice"]

print("Comapny Name:- ",stock.info["longName"])
Number_of_stocks = int((2/100)*float(budget))/int(price)

print("Number of Stocks to buy:-  ",int(Number_of_stocks)+2)
print("Price of the Stock:-  " , price)
print("Total:-  ",price*(Number_of_stocks+1))

start = datetime.today() - timedelta(days = 30)
end = datetime.today()
df = yf.download(ticker,start,end)

df['Close'].plot(label = ticker, figsize = (15,7))
plt.show()
