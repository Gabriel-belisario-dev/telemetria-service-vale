import pandas as pd

# Caminhos dos nossos dois arquivos vitais
TELEMETRIA_LIMPA = "data/telemetria_limpa.parquet"
REGRAS = "data/Alarmes - Regra de Negocio.xlsx"

def analisar_frota():
    print("Iniciando a ignição do Motor de Cruzamento de Dados...")

    # 1. Carregamos o combustível limpo
    df_dados = pd.read_parquet(TELEMETRIA_LIMPA)
    
    # 2. Carregamos as regras e aplicamos a correção de digitação humana (Tudo Maiúsculo)
    df_regras = pd.read_excel(REGRAS, engine='openpyxl')
    df_regras['NIVEL'] = df_regras['NIVEL'].str.upper() 
    
    print("Regras padronizadas com sucesso. Buscando ocorrências reais...")

    # 3. Pegamos a lista de todos os nomes de alarmes que existem no Excel
    eventos_perigosos = df_regras['EVENTO'].unique()
    
    # 4. Filtramos nossos milhões de registros para manter APENAS os alarmes que estão na regra
    # Na base da Vale, o nome do evento fica na coluna 'Alarme'
    ocorrencias_reais = df_dados[df_dados['Alarme'].isin(eventos_perigosos)]
    
    print("\n" + "="*50)
    print(" 🚨 CRUZAMENTO DE DADOS CONCLUÍDO 🚨")
    print("="*50)
    print(f"Dos milhões de registros, encontramos {len(ocorrencias_reais):,} alertas que precisam ser monitorados pelas regras!")
    
    if not ocorrencias_reais.empty:
        print("\n🏆 TOP 5 Caminhões (Tag_Frota) com mais alertas críticos disparados:")
        print(ocorrencias_reais['Tag_Frota'].value_counts().head(5))

if __name__ == "__main__":
    analisar_frota()