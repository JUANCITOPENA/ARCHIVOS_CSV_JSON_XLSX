# Importar las Librerias:
import pandas as pd
import pyodbc
import os

# Configuración de la conexión a SQL Server

server = 'TU SERVIDOR'
database = 'TU BASE DE DATOS'
username = 'TU USARIO'
password = 'TU CLAVE'

# Establecer la conexión

conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Leer datos de SQL Server

query = " SELECT * FROM VISTA_COMPLETA_VENTAS"

df = pd.read_sql(query, conexion)

# Definir rutas de archivos de salida

csv_file= r'TU DIRECTORIO\ARCHIVO_VENTAS_SUPERMERCADO_JPV\DATOS_SUPERMERCADO_JPV.csv'
json_file = r'TU DIRECTORIO\ARCHIVO_VENTAS_SUPERMERCADO_JPV\DATOS_SUPERMERCADO_JPV.json'
excel_file = r'TU DIRECTORIO\ARCHIVO_VENTAS_SUPERMERCADO_JPV\DATOS_SUPERMERCADO_JPV.xlsx'

# Guardar como CSV

df.to_csv(csv_file, index=False)
print(f'Se han guardado los datos en "{csv_file}" satisfactoriamente.')

# Guardar como JSON
df.to_json(json_file, orient='records')
print(f'Se han guardado los datos en "{json_file}" satisfactoriamente.')

# Guardar como Excel
df.to_excel(excel_file, index=False)
print(f'Se han guardado los datos en "{excel_file}" satisfactoriamente.')


# Cerrar la conexión
conexion.close()
print("Conexión cerrada.")