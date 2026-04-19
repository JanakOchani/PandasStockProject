import pandas as pd
import yfinance as yf
from datetime import datetime

class StockProcessor:
    def __init__(self):
        print("Object initialized.")

    def processStocks(self, filename, period):
        self.filename = filename
        self.period = period
        print(f"Stock processor: filename is {filename}, and the time frame is {period}.")

        stock_list = pd.read_csv(filename)
        list_of_stocks = stock_list["ticker"].to_list()
        print(f"Stock processor: list of stocks is {list_of_stocks}.")

        stock_results = []

        for ticker in list_of_stocks:
            print(f"Stock processor: The stock is {ticker}.")
            stock = yf.Ticker(ticker)
            print(f"Stock processor: The stock details from yahoo finance is {ticker}.")

            history = stock.history(period=period)
            print(f"Stock processor: The price history of the stock is {history}.")
            close_prices = history.Close
            print(f"Stock processor: The close price of the stock is {close_prices}.")
            print(f"Stock processor: The average price of the stock is {close_prices.mean()}")

            result = {
                "ticker": ticker,
                "period": period,
                "avg price": round(close_prices.mean(), 2),
                "max price": round(close_prices.max(), 2),
                "min price": round(close_prices.min(), 2),
                "number of days": len(close_prices),
                "analysis date": datetime.now()

            }
            stock_results.append(result)

        stocks_df = pd.DataFrame(stock_results)
        stocks_df.to_csv("stock_info.csv")
        return stocks_df







