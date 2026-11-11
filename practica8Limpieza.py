#PRACTICA 8. LIMPIEZA
#MONICA FERNANDA ALFARO RANGEL

import pyodbc
import pandas as pd
from faker import Faker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine, URL
fake = Faker("es_MX")
Faker.seed(7)

try:
    df= pd.read_csv("Ventas_Originales_alfaro.csv", encoding="utf-8")

except FileNotFoundError:
    print("ERROR: el archivo no existe. Revisa el nombre y la ruta")
except (pd.errors.EmptyDataError, pd.errors.ParserError, UnicodeDecodeError) as error:  
    print("ERROR: el archivo no se puede leer:", error)

else:
    print("INFORMACION DEL ARCHIVO")
    df.info()
    print("Filas:", df.shape[0])
    print("Columnas:", df.shape[1])
    print("RESUMEN ESTADISTIO")
    print(df.describe())

#SI HAY NULOS Y CUANTOS SON   
print("Nulos")
print(df.isnull)
print("Cantidad de valores nulos", df.isnull.sum.sum)

#SI HYAY DUPLICADOS
print("Duplicados")
print(df.duplicated)


#SI HAY CLAVES PRIMARIAS REPETIDAS
print("Claves repetidas")
print(df["id_venta"].duplicated(keep=False))
print("Claves reetidas total", df["id_venta"].duplicated(keep=False).sum())

#CANTIDADES FUERA DEL RANGO (emplea ~ )not
print("Cantidades fuera de rango")


print(df[~df["cantidad"].between(1,10) | df["cantidad"].isna])
cantidades = df["cantidad"]
#############################################
print(df["cantidad"])


print(df[cantidades.between(1,10) | cantidades.isna])


#FECHAS INVALIDAS
print("Fechas invalidas")
print(pd.to_datetime(df["fecha_venta"], errors="coerce"))

#PRODUCTOS INEXISTENTES
productos = pd.DataFrame(
    {
        "id_producto": [1,2,3,4,5,6],
            "producto":["Teclado","Mouse","Monitor","Memoria USB","Camara web","Audifonos"],
            "precio":[350.00,200.00,3500.00,180.00,750.00,600.00],
        
    }
)
print("productos inexistentes")
print(df[df["producto"].isin(productos["id_producto"])])

print(df(subset="id_producto").isin(productos["id_producto"]))
#ACTUALIZAR CANTIDADES POSITIVAS 
df["subtotal"] = df["subtotal"].abs()

#QUITAR FILA DUPLICADA

df.drop_duplicates(keep="first").copy()


#IMPRIMIR CANTIDAD DE REGISTROS

print(df)


