"""Este modulo provee utilidades para la limpieza y normalizacion de datos tipo caracter"""
import unicodedata

def rename_columns(df, new_names):
    """Renombra columnas del DataFrame según el diccionario proporcionado."""
    return df.rename(columns=new_names)

def normalize_text(s):
    """Normaliza y elimina caracteres especiales de una cadena."""
    return unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode('utf-8')

def process_dataframe(df):
    """Limpia las columnas de un DataFrame que tienen caracteres especiales."""
    text_columns = df.select_dtypes(include=['object']).columns
    for col in text_columns:
        if df[col].apply(lambda x: normalize_text(x) != x).any():
            print(f"La columna '{col}' tiene caracteres con tildes o la letra ñ.")
            df[col] = df[col].apply(normalize_text)
        else:
            print(f"La columna '{col}' no tiene caracteres con tildes ni la letra ñ.")
    return df
