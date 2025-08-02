import pandas as pd
import os 

ruta_archivo = './data/ventas.xlsx'

df = pd.read_excel(ruta_archivo)

df['Total']= df['Unidades'] * df['Precio Unitario']

rutas_reportes ='./reportes'

os.makedirs(rutas_reportes, exist_ok=True)

productos = df['Producto'].unique()

for producto in productos:
    df_producto = df[df['Producto']== producto].copy()
    
    total_general = df_producto['Total'].sum()
    
    fila_total = pd.DataFrame([{
        'Fecha': 'TOTAL',
        'Región': '',
        'Producto': '',
        'Vendedor': '',
        'Unidades': df_producto['Unidades'].sum(),
        'Precio unitario': '',
        'Total': total_general 
    }])
    
    df_final = pd.concat([df_producto, fila_total], ignore_index=True)
    
    nombre_archivo = producto.replace(" ", "_") + ".xlsx"
    ruta_salida = os.path.join(rutas_reportes, nombre_archivo)
    
    df_final.to_excel(ruta_salida, index=False)
    print(f"Reporte generado: {ruta_salida}")

print("Todos los reportes fueron generados con totales.")