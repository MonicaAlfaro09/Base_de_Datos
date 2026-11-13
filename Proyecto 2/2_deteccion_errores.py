#Mendoza Costilla Diana Maritza / Alfaro Rangel Monica Fernanda

import pandas as pd
import numpy as np

#1. LIMPIEZA Y EXPORTACIÓN PRODUCTOS 
df_prod = pd.read_csv("productos.csv")
df_prod["nombre"] = df_prod["nombre"].fillna("Sin Nombre").astype(str).str.strip()
df_prod["precio"] = pd.to_numeric(df_prod["precio"], errors='coerce')
df_prod = df_prod[df_prod["precio"] > 0] 
df_prod = df_prod.drop_duplicates(subset=["nombre"]) 
df_prod.to_csv("productos_limpios.csv", index=False, encoding="utf-8-sig")

#2. LIMPIEZA Y EXPORTACIÓN INVENTARIOS
df_inv = pd.read_csv("inventarios.csv")
df_inv["existencia"] = pd.to_numeric(df_inv["existencia"], errors='coerce')
df_inv = df_inv[df_inv["existencia"] >= 0] 
df_inv["ubicacion"] = df_inv["ubicacion"].fillna("Almacén General").astype(str).str.strip()
df_inv = df_inv[df_inv["id_producto"].isin(df_prod["id_producto"])]
df_inv.to_csv("inventarios_limpios.csv", index=False, encoding="utf-8-sig")

# 3. LIMPIEZA Y EXPORTACIÓN PROVEEDORES
df_prov = pd.read_csv("proveedores.csv")
df_prov["nombre"] = df_prov["nombre"].fillna("Proveedor Desconocido").astype(str).str.strip()
df_prov["telefono"] = df_prov["telefono"].astype(str).str.replace(r'\D', '', regex=True)
df_prov = df_prov.drop_duplicates(subset=["nombre"])
df_prov.to_csv("proveedores_limpios.csv", index=False, encoding="utf-8-sig")

print("Proceso ETL finalizado con éxito")