from fastapi import FastAPI, HTTPException
from StockProcessor import StockProcessor
import pandas as pd

priceFundamentals = FastAPI()


@priceFundamentals.get("/")
def root():
    return {"Hello": "PriceFundamentals"}

@priceFundamentals.post("/info")
def analyzeStocks(filename: str, period: str):
    print(f"The file passed is {filename}, and the time frame is {period}.")

    processor = StockProcessor()
    stocks_info_JSON = processor.processStocks(filename, period)
    #return {"FileName": {filename},"Period":{period}}
    return stocks_info_JSON
