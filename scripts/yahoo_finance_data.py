import yfinance as yf

class YahooFinanceData:
    def __init__(self, ticker_symbol):
        """
        Create an object to download stock data from Yahoo Finance.

        *ticker_symbol*: the stock code, for example:
            "SANB11.SA" = Santander B3
            "ITUB4.SA" = Itaú B3
        """
        self.ticker_symbol = ticker_symbol
        self.ticker = yf.Ticker(ticker_symbol)
        self.df_history = None # DataFrame to store downloaded history data

    def download_history(self, period="5y", interval="1d"): # Default to 5 years daily data
        """Download historical stock data"""
        self.df_history = self.ticker.history(period=period, interval=interval)
        return self.df_history


