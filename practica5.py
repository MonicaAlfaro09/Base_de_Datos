#MONICA FERNANDA ALFARO RANGEL

#2. 
import pandas as pd

#3.Emplea el control de errores:
#–Crea una variable llamada datos_csv y lee el archivo proporcionado.
#Emplea el error FileNotFoundError y muestra el mensaje “El archivo no existe”.
try:                
    datos_csv = pd.read_csv("Datos_Ventas_Tienda.csv", encoding='utf-8') 
except FileNotFoundError:
    print("El archivo no existe")


#4.Emplea else en el control de errores y muestra la información de la variable datos_csv y emplea el finally

else:
    print(datos_csv)
finally:
    print("Monica Fernanda Alfaro Rangel")

#5.Muestra si existen registros nulos y ¿cuantos hay?
datos_nulos = datos_csv.isnull().sum().sum()
print(datos_csv)

#6.Ordena los valores empleando el método sort_values()
#–Ordenar por la columna Producto
#–De forma ascendente
print (datos_csv.sort_values(["Producto"], ascending=True))


#7.Quita los espacios vacíos del inicio de los valores de la columna Producto e imprime
datos_csv["Producto"] = datos_csv["Producto"].str.strip()

#8.Convierte el texto en mayúsculas de la columna Producto e imprime
print (datos_csv["Producto"].str.upper())

#9.Convierte el texto en minúsculas de la columna Producto e imprime
print (datos_csv["Producto"].str.lower())


#10.Convierte el texto solo la primera letra en mayúsculas de la columna Producto e imprime

print (datos_csv["Producto"].str.title())

#PLUS SI QUIERO TODAS LAS COLUMNAS EN MAYUSCULAS

print(datos_csv.columns.str.title())
