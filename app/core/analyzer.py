import pandas as pd
import os

TELEMETRIA_LIMPA = "data/telemetria_limpa.parquet"
REGRAS = "data/Alarmes - Regra de Negocio.xlsx"

def obter_caminhoes_risco_temporal():
    # Carrega dados
    df_dados = pd.read_parquet(TELEMETRIA_LIMPA)
    df_regras = pd.read_excel(REGRAS, engine='openpyxl')
    
    # Prepara a data e o dicionário de resultados
    df_dados['Data_Evento'] = pd.to_datetime(df_dados['Data_Evento'])
    caminhoes_criticos = {}
    total_infracoes = 0

    # Aplica a Janela Deslizante (Rolling Window)
    for index, regra in df_regras.iterrows():
        evento = regra['EVENTO']
        qtd_maxima = int(regra['QTD'])
        tempo_limite = int(regra['TEMPO'])

        df_evento = df_dados[df_dados['Alarme'] == evento].copy()
        if df_evento.empty or qtd_maxima <= 1:
            continue

        df_evento = df_evento.sort_values(by=['Tag_Frota', 'Data_Evento'])
        df_evento['Tempo_Passado'] = df_evento.groupby('Tag_Frota')['Data_Evento'].diff(periods=qtd_maxima - 1)
        df_evento['Minutos'] = df_evento['Tempo_Passado'].dt.total_seconds() / 60.0
        
        infracoes = df_evento[df_evento['Minutos'] <= tempo_limite]

        if not infracoes.empty:
            total_infracoes += len(infracoes)
            contagem = infracoes['Tag_Frota'].value_counts()
            for caminhao, qtd in contagem.items():
                caminhoes_criticos[caminhao] = caminhoes_criticos.get(caminhao, 0) + qtd

    # Ordena os Top 5
    top_5 = dict(sorted(caminhoes_criticos.items(), key=lambda item: item[1], reverse=True)[:5])
    
    return {
        "total_infracoes_confirmadas": total_infracoes,
        "top_5_criticos": top_5
    }