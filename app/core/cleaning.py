import pandas as pd
import os

PASTA_TELEMETRIA = "data/telemetria/"

def limpar_dados_telemetria():
    print("Iniciando pipeline de limpeza e correção da telemetria...")
    arquivos = [f for f in os.listdir(PASTA_TELEMETRIA) if f.endswith('.parquet')]
    
    if not arquivos:
        print("Erro: Nenhum arquivo .parquet encontrado na pasta!")
        return

    arquivo_alvo = os.path.join(PASTA_TELEMETRIA, arquivos[0])
    df = pd.read_parquet(arquivo_alvo)
    
    print("Corrigindo a 'pegadinha' da Vale: Convertendo vírgulas para pontos...")
    df['Valor'] = df['Valor'].astype(str).str.replace(',', '.')
    
    # Força a conversão para número
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    
    # Remove o que realmente era lixo irrecuperável
    df = df.dropna(subset=['Valor'])
    
    # Salva o arquivo novo e limpo!
    caminho_limpo = "data/telemetria_limpa.parquet"
    df.to_parquet(caminho_limpo)
    print(f"\n✅ Sucesso total! Base limpa e salva em: {caminho_limpo}")

if __name__ == "__main__":
    limpar_dados_telemetria()