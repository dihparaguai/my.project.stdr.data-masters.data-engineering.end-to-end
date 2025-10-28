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


## Project Structure:
root_project/
│
├── docs/               # Project documentation, diagrams, specifications
│
├── notebooks/          # Exploration and testing notebooks
│
├── scripts/            # ETL scripts, functions, automation
│
└── README.md           # Project overview and instructions


## Architecture
1. **Data Sources**
   - Yahoo Finance API
   - Alpha Vantage API
2. **Data Ingestion**
   - APIs run in Docker containers.
   - Data goes straight to the Bronze layer in MinIO.
3. **Data Processing**
   - Data moves through layers: Bronze → Silver → Gold.
   - Applies cleaning, transforming, and aggregating.
4. **Data Storage**
   - Gold layer is loaded into PostgreSQL.
5. **Data Analysis**
   - Power BI reads data from PostgreSQL for dashboards and reports.