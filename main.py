import os
from utils.download import download_data
from utils.read import read_data_from_csv, read_data_from_local_file
from utils.process import rename_columns, process_dataframe
from utils.filter import filter_by_column
from utils.export import export_data

def main():
    
    url = (
        "https://www.datos.gov.co/api/views/yhxn-eqqw/rows.csv?accessType=DOWNLOAD"
    )
    csv_text=download_data(url)

    local_file_path = os.path.join('data', 'data.csv')

    if not csv_text:  # Si la descarga falla, intenta leer desde un archivo local
        print("Intentando leer desde archivo local...")
        try:
            df = read_data_from_local_file(local_file_path)
        except FileNotFoundError:
            print(f"Archivo local no encontrado en {local_file_path}.")
            return
    else:
        df = read_data_from_csv(csv_text)

    while True:
        print("\nMenu de Opciones:")
        print("1. Preprocesar la data")
        print("2. Filtrar por género")
        print("3. Filtrar por cualquier otra columna")
        print("4. Mostrar conteo de víctimas por año, mes, departamento, actividad, género o estado")
        print("5. Salir")
        option = input("Seleccione una opción: ")

        if option == '1':
            
            df = rename_columns(df, {'genero': 'estado', 'estado': 'genero'})
            df = process_dataframe(df)
            
            column_order = [
                'genero', 'rangoedad', 'estado', 'Actividad', 'condicion', 
                'grupoetnico', 'tipoevento', 'Ubicación', 'municipio', 
                'departamento', 'sitio', 'latitudcabecera', 
                'longitudcabecera', 'tipoarea', 'ano', 'mes', 
                'codigodanemunicipio', 'codigodanedepartamento'
            ]
            
            df = df.reindex(columns=column_order)
            export_data(df, 'processed_data.csv')
            print("Los datos han sido limpiados y exportados.")

        elif option == '2':
            
            genre_user = input(
            """Ingresar género (Hombre o Mujer): """
            ).capitalize()
            
            df_filtered = df.loc[df['genero'] == genre_user]
            
            export_data(
                df_filtered, 
                f'genero_{genre_user}.csv'
            )
            print(df_filtered.tail())

        elif option == '3':
            
            column_name = input(
            """Ingresa el nombre de la columna para filtrar: """
            ).lower()

            value = input(
            f"""Ingresa un valor de {column_name} para filtrar: """
            )
            
            df_filtered = filter_by_column(df, column_name, value)
            print(df_filtered)

            export_data(
                df_filtered, 
                f"""filtered_by_{column_name}_{value}.csv"""
            )

            print(
                f"""Datos filtrados por '{column_name}' = '{value}' 
                exportados a 'data/filtered_by_{column_name}_{value}.csv'."""
                )

            print(df.head())


        elif option == '4':
            os.system('python script.py')

        elif option == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
