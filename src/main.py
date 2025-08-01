import pandas as pd

ruta_archivo = './data/ventas.xlsx'

df = pd.read_excel(ruta_archivo)

print("Datos cargados correctamente: ")
print(df.head())