from fastapi import FastAPI
import pandas as pd

app = FastAPI(
    title="API de Telemetria e Monitoramento - Vale",
    description="Motor preditivo para análise de frota de caminhões.",
    version="1.0.0"
)

# Caminhos dos dados locais
TELEMETRIA_LIMPA = "data/telemetria_limpa.parquet"
REGRAS = "data/Alarmes - Regra de Negocio.xlsx"

@app.get("/")
def home():
    return {"status": "Motor da API ligado e operando com sucesso!"}

@app.get("/analise/top-caminhoes")
def obter_caminhoes_criticos():
    """
    Cruza a base de telemetria limpa com as regras de negócio
    e retorna o Top 5 de caminhões com mais alertas de perigo.
    """
    # Carrega dados
    df_dados = pd.read_parquet(TELEMETRIA_LIMPA)
    df_regras = pd.read_excel(REGRAS, engine='openpyxl')
    
    # Padroniza as regras
    df_regras['NIVEL'] = df_regras['NIVEL'].str.upper()
    eventos_perigosos = df_regras['EVENTO'].unique()
    
    # Filtra as ocorrências reais
    ocorrencias_reais = df_dados[df_dados['Alarme'].isin(eventos_perigosos)]
    
    # Conta os top 5 e converte para um formato que a API entende (Dicionário)
    top_5 = ocorrencias_reais['Tag_Frota'].value_counts().head(5).to_dict()
    
    return {
        "total_alertas_encontrados": len(ocorrencias_reais),
        "ranking_caminhoes_criticos": top_5
    }