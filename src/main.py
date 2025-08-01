import pandas as pd
import os 

ruta_archivo = './data/ventas.xlsx'

df = pd.read_excel(ruta_archivo)

ruta_reportes = "./reportes"
os.makedirs(ruta_reportes, exist_ok = True)

productos = df['Producto'].unique()

for producto in productos:
    df_producto = df[df['Producto'] == producto]
    ruta_salida = os.path.join(ruta_reportes, f"{producto}.xlsx")
    df_producto.to_excel(ruta_salida, index = False)
    print(f"Reporte generado: {ruta_salida}")
    
print("Todos los reportes fueron generados")