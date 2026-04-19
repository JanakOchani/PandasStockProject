This project is a backend application implemented with an API created with FastAPI and is designed to analyze stock price data 
using live information provided by the yfinance library. In brief, a CSV file with stock tickers is accepted as an input, 
loaded using pandas, and processed for each stock from the StockProcessor class. 
For each stock, the application fetches historical prices for a certain time period chosen by the user, calculates some statistics 
including average close, maximum, minimum values, total days of trading as well as the date of analysis, packs all the output in 
an organized structure, outputs it to the client as a JSON object through the API, and saves in CSV format as well.

Overall, the project's implementation has two major parts – the FastAPI application in api.py, 
and the StockProcessor class in StockProcessor.py where all the calculations take place.

Pandas is a very useful module in the programming language Python which serves the purpose of data manipulation. 
The use of this library in this project is that it reads the input CSV file having the tickers of stocks in it and creates a 
DataFrame out of it. It also assists in the management and transformation of data received from yfinance so that 
calculations like average, maximum, and minimum can be easily calculated.

https://pandas.pydata.org/



