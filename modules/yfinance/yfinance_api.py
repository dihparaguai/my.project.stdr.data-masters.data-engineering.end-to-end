# modules/yfinance/yfinance_api.py

import os
from datetime import datetime, timedelta
import yfinance as yf

class YFinanceAPI:
    def __init__(self, ticker_symbol):
        """
        Create an object to download stock data from Yahoo Finance.

        *ticker_symbol*: the stock code, for example:
            "SANB11.SA" = Santander B3
            "ITUB4.SA" = Itaú B3
        """
        self.ticker = yf.Ticker(ticker_symbol)


    def download_history(self, date: str):
        """Download historical stock data"""
        end_date = (datetime.strptime(date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")

        df = self.ticker.history(start=date, end=end_date, interval="15m")
        return df

    
    def save_to_csv(self, df, date: str, path: str):
        """Salva dataframe no caminho correto"""
        path = os.path.join(path, self.ticker)
        os.makedirs(path, exist_ok=True)

        file_name = f"{self.ticker}_raw_{date}.csv"

        df.to_csv(os.path.join(path, file_name), index=False)