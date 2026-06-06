from fastapi import FastAPI
from app.core.analyzer import obter_caminhoes_risco_temporal

app = FastAPI(
    title="API de Telemetria e Monitoramento - Vale",
    description="Motor preditivo com Janela Deslizante (Rolling Window).",
    version="2.0.0"
)

@app.get("/")
def home():
    return {"status": "Motor da API ligado e operando com sucesso!"}

@app.get("/analise/top-caminhoes")
def ranking_risco():
    """
    Retorna o Top 5 caminhões com risco de falha iminente, 
    calculado através de regras temporais (Rolling Window).
    """
    resultado = obter_caminhoes_risco_temporal()
    return resultado