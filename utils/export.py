"""Este módulo contiene funciones para exportar datos a archivos CSV y archivos de texto."""
import os

def export_data(df, file_name):
    """Exporta los datos a un archivo CSV en la carpeta 'data'."""
    if not os.path.exists('data'):
        os.makedirs('data')
    file_path = os.path.join('data', file_name)
    df.to_csv(file_path, index=False)
    print(f"Datos exportados correctamente a: {file_path}")


def export_totals(totals, file_name):
    """Exporta los totales como texto en un archivo."""
    file_path = os.path.join(file_name)

    with open(file_path, 'w', encoding='utf-8') as f:
        for category, counts in totals.items():
            f.write(f"{category.replace('_', ' ').title()}:\n")
            for key, value in counts.items():
                f.write(f"{key}: {value}\n")

    print(f"Totales exportados correctamente a: {file_path}")
    