# modules/yfinance/yfinance_api.py

import os
from datetime import datetime, timedelta
import yfinance as yf

class YFinanceAPI:
    def __init__(self, ticker_symbol: str):
        """
        Create an object to download stock data from Yahoo Finance.

        *ticker_symbol*: the stock code, for example:
            "SANB11.SA" = Santander B3
            "ITUB4.SA" = Itaú B3
        """
        self.ticker_symbol = ticker_symbol
        self.ticker = yf.Ticker(self.ticker_symbol)
        


    def download_history(self, date: str):
        """
        Download historical stock data
        """
        end_date = (datetime.strptime(date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")

        df = self.ticker.history(start=date, end=end_date, interval="15m")

        if df.empty:
            return None
        
        return df

    
    def save_to_csv(self, df, date: str, path: str):
        """
        Save dataframe to local storage
        """
        path = os.path.join(path, self.ticker_symbol)
        os.makedirs(path, exist_ok=True)

        file_name = f"{self.ticker}_raw_{date}.csv"

        if df is None or df.empty:
            print(f"There is no data in {date} to save.")
        return

        df.to_csv(os.path.join(path, file_name), index=False)