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
        "budget":[budget],
        "Current Price":[pd.NA],
        "Change Percent":[pd.NA]
       }


df = pd.DataFrame(dict)
def current_price_calc(calc):
    Company = yf.Ticker(calc["Ticker"])
    return Company.info['currentPrice']

def change_price(price):
    return (float(price["Current Price"])-float(price["Price_Bought"]))/100

account = pd.read_csv("data/accounts.csv")
df = df.append(account, ignore_index = True)
df["Current Price"] = df.apply(current_price_calc,axis = 1)
df["Change Percent"] = df.apply(change_price,axis = 1)

df.to_csv("data/accounts.csv" , index = False)
