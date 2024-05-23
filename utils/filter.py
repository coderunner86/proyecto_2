"""Este módulo contiene funciones para filtrar DataFrames basados en el valor de una columna."""

import pandas as pd
from utils.process import normalize_text

def filter_by_column(df, column_name, value):
    """Filtra el DataFrame por el valor de una columna."""
    column_name = column_name.lower()
    columns = [col.lower() for col in df.columns]
    if column_name in columns:
        actual_column_name = df.columns[columns.index(column_name)]
        normalized_value = normalize_text(value)
        df[actual_column_name] = df[actual_column_name].apply(normalize_text)
        return df.loc[df[actual_column_name] == normalized_value]

    print(f"Columna '{column_name}' no encontrada en el DataFrame.")
    return pd.DataFrame()
