#Monica Fernanda Alfaro Rangel


#1. Importa la biblioteca pandas.
import pandas as pd

#2. Crea una variable llamada datos_csv y carga el archivo CSV
datos_csv = pd.read_csv("envios_logisticas.csv")

#3. Muestra la información general del DataFrame utilizando el método adecuado.
print(datos_csv.info())

#4. Muestra los primeros seis registros del archivo.
print(datos_csv.head(6))

#5. Muestra los últimos cinco registros del archivo.
print(datos_csv.tail(5))

#6. Imprime el número de filas y columnas.
print(datos_csv.shape)

#7. Muestra los nombres de las columnas.
print(datos_csv.columns)

#8. Muestra el tipo de dato de cada columna.
print(datos_csv.dtypes)

#9. Muestra si existen valores nulos y cuántos hay con el método isnull().sum()
print(datos_csv.isnull().sum())

#10. Investiga y escribe como comentario para que sirven los métodos fillna() y dropna()
#sirven para manejar valores nulos o faltantes (NaN) en 
# un conjunto de datos (DataFrame o Series).