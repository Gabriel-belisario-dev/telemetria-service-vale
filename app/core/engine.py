import pandas as pd
import os

CAMINHO_REGRAS = "data/Alarmes - Regra de Negocio.xlsx"

def carregar_regras_negocio():
    print("Iniciando o carregamento da Inteligência Preditiva...")
    
    if not os.path.exists(CAMINHO_REGRAS):
        print("Erro: Arquivo de regras não encontrado na pasta data!")
        return None
        
    # O engine 'openpyxl' é necessário para ler .xlsx
    df_regras = pd.read_excel(CAMINHO_REGRAS, engine='openpyxl')
    
    print("\n" + "="*50)
    print(" 🧠 MOTOR DE REGRAS VALE CARREGADO 🧠")
    print("="*50)
    print(f"Total de regras de segurança mapeadas: {len(df_regras)}")
    
    print("\nVisão geral das colunas interpretadas:")
    print(df_regras.columns.tolist())
    
    print("\nExemplo das 3 primeiras regras táticas (Rolling Windows):")
    # Mostramos apenas as colunas vitais para a lógica
    print(df_regras[['EVENTO', 'QTD', 'TEMPO', 'NIVEL']].head(3))
    
    return df_regras

if __name__ == "__main__":
    carregar_regras_negocio()