import requests
import pandas as pd

class AlphaVantageData:
    def __init__(self, api_key, symbol):
        """
        Create an object to download stock data from Alpha Vantage.

        *api_key*: your Alpha Vantage API key  
        *symbol*: stock symbol, for example: 
            "MSFT" = Microsoft

        _Note: Alpha Vantage does not support Brazilian stocks like "SANB11.SA" or "ITUB4.SA"._
        """
        self.api_key = api_key
        self.symbol = symbol
        self.url = "https://www.alphavantage.co/query"
        self.df = None  # DataFrame to store downloaded data

    def download_points(self):
        """
        Download intraday stock data from Alpha Vantage.

        *outputsize*: "compact" = last 100 data points, "full" = full history
        """
        params = {
            "function": "TIME_SERIES_INTRADAY", # Intraday data (minute by minute)
            "symbol": self.symbol,
            "interval": "1min", # Each point represents 1 minute
            "outputsize": "compact",
            "datatype": "json",
            "apikey": self.api_key
        }

        response = requests.get(self.url, params=params) # Send a GET request to the Alpha Vantage API
        data = response.json() # Convert the API response from JSON format to a Python dictionary

        # Get only the Time Series data from the JSON, ignoring the Meta Data
        time_series_key = f"Time Series ({params['interval']})"
        time_series = data.get(time_series_key, {})

        # Convert JSON to DataFrame
        df = pd.DataFrame(time_series).T.reset_index() # Transpose and transform index into column
        df = df.rename(columns={"index": "timestamp"}) # Rename the index column to "timestamp"
        df["timestamp"] = pd.to_datetime(df["timestamp"]) # Convert timestamp strings to datetime
        df[df.columns.difference(["timestamp"])] = df[df.columns.difference(["timestamp"])].astype(float) # Convert all other columns to float (skip timestamp)

        self.df = df
        return df