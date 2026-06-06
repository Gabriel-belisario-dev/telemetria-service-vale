import pandas as pd
import os

PASTA_TELEMETRIA = "data/telemetria/"

def mapear_sujeira_telemetria():
    print("Iniciando varredura na pasta de telemetria...")
    arquivos = [f for f in os.listdir(PASTA_TELEMETRIA) if f.endswith('.parquet')]
    
    if not arquivos:
        print("Erro: Nenhum arquivo .parquet encontrado!")
        return

    arquivo_alvo = os.path.join(PASTA_TELEMETRIA, arquivos[0])
    print(f"Arquivo encontrado: {arquivo_alvo}")
    
    df = pd.read_parquet(arquivo_alvo)
    
    print("\n" + "="*50)
    print(" 🚨 CAÇANDO ERROS DE TIPAGEM NA COLUNA 'VALOR' 🚨")
    print("="*50)
    
    # 1. Tenta converter a coluna inteira para número. 
    # O 'coerce' transforma o que for texto (erro) em NaN (Nulo)
    valores_convertidos = pd.to_numeric(df['Valor'], errors='coerce')
    
    # 2. Filtra o dataframe original apenas onde a conversão falhou
    linhas_com_erro = df[valores_convertidos.isna()]
    
    total_erros = len(linhas_com_erro)
    
    if total_erros > 0:
        print(f"ALERTA CRÍTICO: Encontramos {total_erros:,} registros com sujeira na coluna 'Valor'!")
        print("\nExemplos do lixo encontrado nos sensores (em vez de números):")
        
        # Pega os valores únicos que causaram o erro para a gente ver o que é
        sujeiras_unicas = linhas_com_erro['Valor'].unique()
        print(sujeiras_unicas[:15]) # Mostra os primeiros 15 tipos de erro
        
    else:
        print("Nenhum erro de texto encontrado na coluna Valor.")

if __name__ == "__main__":
    mapear_sujeira_telemetria()