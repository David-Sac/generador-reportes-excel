# Generador de Reporte Automáticos en Excel

Este proyecto autommatiza la lectura de datos desde un archivo Excel y genera reportes individuales por categoría (ej. por producto, región, etc.).

## Funcionalidades

- Lee datos desde un archivo Excel
- Agrupa por producto
- Calcula totales por producto (unidades y ventas)
- Genera un archivo Excel por producto en la carpeta 'reportes/'

## Tecnologías usadas

- Python 3
- Pandas
- OpenPyXL

## Filtros disponibles

Puedes ejecutar el script con los siguientes argumentos:

| Opción      | Descripción                             | Ejemplo                          |
|-------------|-----------------------------------------|----------------------------------|
| `--region`  | Filtra por región                       | `--region Norte`                 |
| `--desde`   | Fecha inicial (`YYYY-MM-DD`)            | `--desde 2025-08-01`             |
| `--hasta`   | Fecha final (`YYYY-MM-DD`)              | `--hasta 2025-08-03`             |

### Ejemplos de uso:

python main.py --region Norte
python main.py --desde 2025-08-01 --hasta 2025-08-03