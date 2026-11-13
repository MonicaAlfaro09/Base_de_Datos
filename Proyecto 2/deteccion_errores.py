# Código realizado por: Mendoza Costilla Diana Maritza y Alfaro Rangel Monica Fernanda
import pandas as pd

def analizar_csv(archivo, nombre_tabla):
    print(f"=== ANALIZANDO: {nombre_tabla} ({archivo}) ===")
    df = pd.read_csv(archivo)
    total_registros = len(df)
    
    # 1. Detección de Nulos
    nulos = df.isnull().sum().sum()
    
    # 2. Detección de Duplicados Exactos
    duplicados = df.duplicated().sum()
    
    # 3. Detección de Espacios en Blanco
    espacios = 0
    for col in df.select_dtypes(include=['object', 'string']).columns:
        serie_texto = df[col].fillna('').astype(str)
        espacios += (serie_texto != serie_texto.str.strip()).sum()
        
    print(f"Total Registros: {total_registros}")
    print(f"Campos Nulos Encontrados: {nulos}")
    print(f"Registros Duplicados Exactos: {duplicados}")
    print(f"Registros con Espacios Inconsistentes: {espacios}\n")

analizar_csv("productos.csv", "Productos")
analizar_csv("inventarios.csv", "Inventarios")
analizar_csv("proveedores.csv", "Proveedores")


# Exportación de los DataFrames limpios a archivos CSV
df_prod.to_csv("productos_limpios.csv", index=False, encoding="utf-8-sig")[cite: 2]
df_inv.to_csv("inventarios_limpios.csv", index=False, encoding="utf-8-sig")[cite: 2]
df_prov.to_csv("proveedores_limpios.csv", index=False, encoding="utf-8-sig")[cite: 2]

print("Exportación completada exitosamente sin columnas de índice.")