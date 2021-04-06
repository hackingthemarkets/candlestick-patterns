import yfinance as yf

pizza = yf.Ticker("pzza")

dataframe = pizza.history(period="1y")

print(dataframe.to_csv())