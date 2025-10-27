## Tema:
Desenvolvimento de pipeline de engenharia de dados voltado ao setor bancário, usando dados de ações de grandes bancos da B3, com foco em ingestão e estruturação de dados financeiros, para simular flixos em batch e em streaming.
O objetivo é inicial é construir uma base de dados que permita análises históricas e em tempo quase real, simulando cenários reais de um pipeline de engenharia de dados.

## Fonte de dados:
- Santander (SANB11\.SA): dados histórios extraídos do Yahoo Finance, em formato CSV, representado o fluxo batch.
    - (https://ranaroussi.github.io/yfinance/) 
- Itaú (ITUB3\.SA): dados intraday (em vários momentos no mesmo dia) extraidos pela API Alpha Vantage, em formato JSON, representando o flixo streaming.
    - (https://www.alphavantage.co/query)