import pandas as pd
import yfinance as yf
from datetime import datetime


ticker = input("Enter the Ticker:-  ")
Company = yf.Ticker(ticker)

company_name = Company.info['longName']
price_bought = input("Price Bought:-  ")
quantity = input("quantity:-  ")
total = float(price_bought) * float(quantity)
budget = input('Budget:-  ')

dict = {'Date':[datetime.today()],
        'Ticker':[ticker],
        'Name':[company_name],
        'Price_Bought':[price_bought],
        'quantity':[quantity],
        'total_price':[total],
        "budget":[budget]
       }

df = pd.DataFrame(dict)
account = pd.read_csv("data/accounts.csv")
df = df.append(account, ignore_index = True)
df.to_csv("data/accounts.csv" , index = False)
