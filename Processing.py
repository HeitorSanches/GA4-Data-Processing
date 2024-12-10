def leitura_dados_ga(dados, experimento):
    import pandas as pd

    # Leitura e tratamento inicial dos dados
    df = pd.read_csv(dados, skiprows=7)
    df = df.drop('Total geral', axis=1)
    df = df.rename(columns={'Unnamed: 0': 'variante'})
    df.columns.values[1] = 'Ocorrências'

    # Aplicação de lógica baseada no experimento fornecido
    df['variante'] = df['variante'].apply(
        lambda x: f"{experimento}_a" if f"{experimento}_a" in x else
        (f"{experimento}_b" if f"{experimento}_b" in x else None)
    )
    
    # Agrupamento e soma por variante
    df = df.groupby('variante').sum().reset_index()

    return df
