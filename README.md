# 🚀 API Analítica de Telemetria - Frota Off-Highway

Este projeto é um microsserviço de backend desenvolvido em **Python (FastAPI)** focado em análise preditiva de telemetria. O sistema ingere milhões de registros de sensores de caminhões, higieniza os dados e aplica lógicas de **Rolling Window (Janela Deslizante)** para alertar riscos iminentes de falhas mecânicas.

## 🧠 A Arquitetura da Solução

O desafio consistiu em transformar mais de 37 milhões de registros brutos em inteligência acionável, dividindo o processo em duas etapas vitais:

### 1. Data Cleansing e o "Mistério dos Sensores"
Durante a ingestão inicial do arquivo `.parquet`, a engine não reconhecia as medições como numéricas. Uma investigação mais profunda nos dados revelou que os sensores exportaram as informações de leitura utilizando a localização PT-BR (vírgulas em vez de pontos, ex: `55,5`). 
* **Solução:** Foi construído um pipeline de limpeza (`cleaning.py`) com vetorização via Pandas que substituiu os caracteres, forçou a tipagem correta e isolou as linhas irrecuperáveis, gerando um novo arquivo sanitizado para o motor principal.

### 2. O Cérebro: Janela Deslizante (Rolling Window)
Um alarme isolado não significa, necessariamente, uma falha catastrófica. O sistema precisava interpretar regras de tempo e repetição.
* **A Lógica:** Construímos um motor que agrupa os dados por caminhão e ordena cronologicamente. Ele calcula a diferença de tempo entre os erros e cruza com a matriz de segurança.
* **O Impacto:** Conseguimos isolar os falsos positivos. O sistema reduziu **15.766** alertas brutos para apenas **14.135** riscos confirmados, indicando os equipamentos exatos que devem sofrer interrupção (*Don't Go*).

## 🛠️ Tecnologias Utilizadas
* **FastAPI:** Exposição da inteligência via endpoints performáticos.
* **Pandas & PyArrow:** Processamento pesado de Big Data e leitura do formato Parquet.
* **OpenPyXL:** Leitura e tradução das regras de negócio.
* **Uvicorn:** Servidor ASGI para rodar a aplicação.

## 🚀 Como Executar Localmente

1. Clone o repositório.
2. Instale as dependências listadas no arquivo `requirements.txt`:
   `pip install -r requirements.txt`
3. Inicie o servidor da API:
   `uvicorn app.main:app --reload`
4. Acesse a documentação interativa e execute o cálculo preditivo através do Swagger UI:
   `http://127.0.0.1:8000/docs`