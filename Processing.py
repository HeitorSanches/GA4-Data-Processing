import pandas as pd

def leitura_dados_ga(dados, experimento):
    df = pd.read_csv(dados, skiprows=7)
    if 'Total geral' in df.columns:
        df = df.drop('Total geral', axis=1)

    df = df.rename(columns={'Unnamed: 0': 'variante'})
    if len(df.columns) > 1:
        df.columns.values[1] = 'Ocorrências'
    
    variantes_validas = [f"{experimento}_a", f"{experimento}_b", f"{experimento}_c"]

    df['variante'] = df['variante'].str.lower().apply(
        lambda x: next((v for v in variantes_validas if v in x.lower()), x)
    )
    
    df = df.groupby('variante', as_index=False).sum()

    return df
