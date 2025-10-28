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
        self.history = None
        self.dividends = None

    def download_history(self):
        """Download historical stock data"""
        self.history = self.ticker.history(period="5y")
        return self.history

    def download_dividends(self):
        """Download dividend payments"""
        self.dividends = self.ticker.dividends
        return self.dividends


