"""Este script realiza calculos automaticos sobre los datos procesados"""
import os
from utils.read import read_data_from_local_file
from utils.export import export_totals

def calculate_totals(df):
    """Calcula totales por diferentes categorías en el DataFrame."""
    totals = {
        'total_victimas_por_ano': df['ano'].value_counts().to_dict(),
        'total_victimas_por_mes': df['mes'].value_counts().to_dict(),
        'total_victimas_por_departamento': df['departamento'].value_counts().to_dict(),
        'total_victimas_por_actividad': df['Actividad'].value_counts().to_dict(),
        'total_victimas_por_genero': df['genero'].value_counts().to_dict(),
        'total_victimas_por_estado': df['estado'].value_counts().to_dict(),
    }
    return totals

def display_totals(totals):
    """Muestra los totales calculados en la consola."""
    for category, counts in totals.items():
        print(f"\n{category.replace('_', ' ').title()}:")
        for key, value in counts.items():
            print(f"{key}: {value}")

def main():
    """This is the main method"""
    local_file_path = os.path.join('data', 'processed_data.csv')

    try:
        df = read_data_from_local_file(local_file_path)
    except FileNotFoundError:
        print(f"Archivo procesado no encontrado en {local_file_path}.")
        return

    totals = calculate_totals(df)
    display_totals(totals)

    totals_file_path = os.path.join('data', 'resultados.txt')
    export_totals(totals, totals_file_path)

if __name__ == "__main__":
    main()
