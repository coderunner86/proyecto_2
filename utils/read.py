import pandas as pd
import io

def read_data_from_csv(csv_text):
    """Convierte texto CSV a DataFrame."""
    return pd.read_csv(io.StringIO(csv_text))

def read_data_from_local_file(file_path):
    """Lee datos desde un archivo local CSV."""
    return pd.read_csv(file_path)
