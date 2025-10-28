[README PT-BR](README.pt-br.md)

## Theme:
Development of a data engineering pipeline focused on the banking sector, using stock market data from major Brazilian banks listed on B3.
The project focuses on data ingestion and structuring of financial data, simulating both batch and streaming data flows.
The main goal is to build a database that supports historical and near real-time analyses, replicating real-world data engineering scenarios.

## Data Sources:
- Santander (SANB11.SA): Historical data extracted from Yahoo Finance, in CSV format, representing the batch data flow.
    - [Yahoo Finance API](https://ranaroussi.github.io/yfinance/) 
- Intraday data (several points within the same day) extracted using the Alpha Vantage API, in JSON format, representing the streaming data flow.
    - [Alpha Vantage API](https://www.alphavantage.co/query)