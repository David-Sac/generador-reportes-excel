import pandas as pd
import os
import argparse

def generar_reportes(region=None, desde=None, hasta=None):
    
    ruta_archivo = '../data/ventas.xlsx'
    
    df = pd.read_excel(ruta_archivo)
    
    df['Total'] = df['Unidades'] * df['Precio Unitario']
    
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    if region:
        df = df[df['Región'].str.lower() == region.lower()]
    if desde:
        df = df[df['Fecha'] >= pd.to_datetime(desde)]
    if hasta: 
        df = df[df['Fecha'] <= pd.to_datetime(hasta)]
        
    ruta_reportes = '../reportes'
    os.makedirs(ruta_reportes, exist_ok=True)
    
    if df.empty:
        print("No hay datos para los filtros aplicados.")
        return
    
    productos = df['Producto'].unique()
    
    for producto in productos:
        df_producto = df[df['Producto']  == producto].copy()
        
        total_general = df_producto['Total'].sum()
        
        fila_total = pd.DataFrame([{
            'Fecha': 'TOTAL',
            'Región': '',
            'Producto': '',
            'Vendedor': '',
            'Unidades': df_producto['Unidades'].sum(),
            'Precio Unitario': '',
            'Total': total_general
        }])
        
        df_final = pd.concat([df_producto, fila_total], ignore_index=True)

        nombre_archivo = producto.replace(" ", "_") + ".xlsx"
        ruta_salida = os.path.join(ruta_reportes, nombre_archivo)

        df_final.to_excel(ruta_salida, index=False)
        print(f"Reporte generado: {ruta_salida}")
        
    print("Todos los reportes fueron generados con filtros aplicados.")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generador de reportes Excel por productos.")
    parser.add_argument("--region", help="Filtrar por región (Ej: Norte)")
    parser.add_argument("--desde", help="Fecha inicial (Ej: 2025-08-01)")
    parser.add_argument("--hasta", help="Fecha final (Ej: 2025-08-03)")
    args = parser.parse_args()
    
    generar_reportes(region=args.region, desde=args.desde, hasta=args.hasta)
