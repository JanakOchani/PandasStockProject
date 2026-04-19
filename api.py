from fastapi import FastAPI, HTTPException
from StockProcessor import StockProcessor
from Database import Database
import pandas as pd

priceFundamentals = FastAPI()


@priceFundamentals.get("/")
def root():
    return {"Hello": "PriceFundamentals"}


@priceFundamentals.post("/info")
def analyzeStocks(filename: str, period: str):
    processor = StockProcessor()
    stocks_df = processor.processStocks(filename, period)
    db = Database()
    db.storeStockData(stocks_df)
    return stocks_df.to_json()