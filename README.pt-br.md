[README EN-US](README.md)


## Tema:
Desenvolvimento de pipeline de engenharia de dados voltado ao setor bancário, usando dados de ações do Satander, Itau e Microsoft, com foco em ingestão e estruturação de dados financeiros, para simular flixos em batch e em streaming.
O objetivo inicial é construir uma base de dados que permita análises históricas e em tempo quase real, simulando cenários reais de um pipeline de engenharia de dados.


## Fonte de dados:
- Santander (SANB11.SA): dados históricos extraídos da API Yahoo Finance, em formato DataFrame do Pandas, representando o fluxo batch.
   - [Yahoo Finance API](https://ranaroussi.github.io/yfinance/) 
- Itaú (ITUB3.SA): dados intraday (vários momentos no mesmo dia) extraídos da API Yahoo Finance, em formato DataFrame do Pandas, representando o fluxo streaming.
   - [Yahoo Finance API](https://ranaroussi.github.io/yfinance/) 
- Microsoft (MSFT): dados intraday (vários momentos no mesmo dia) extraídos da API Alpha Vantage, em formato JSON, representando o fluxo streaming.
   - [Alpha Vantage API](https://www.alphavantage.co/query)


## Estrutura do projeto:
proj_raíz/
│
├── docs/               # Documentação do projeto, diagramas, especificações
│
├── notebooks/          # Notebooks de exploração e testes
│
├── scripts/            # Scripts de ETL, funções, automações
│
└── README.md           # Visão geral do projeto e instruções


## Arquitetura
1. **Fontes de Dados**
   - Yahoo Finance API
   - Alpha Vantage API
2. **Ingestão de Dados**
   - APIs rodam em containers Docker.
   - Os dados vão direto para a camada Bronze no MinIO.
3. **Processamento de Dados**
   - Os dados seguem pelas camadas: Bronze → Prata → Ouro.
   - Aplica limpeza, transformação e agregação.
4. **Armazenamento de Dados**
   - A camada Ouro é carregada no PostgreSQL.
5. **Análise de Dados**
   - O Power BI acessa o PostgreSQL para criar dashboards e relatórios.
