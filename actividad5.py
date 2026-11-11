#MONICA FERNANDA ALFARO RANGEL  



# 1.  Importa la biblioteca pandas.
import pandas as pd
# •2. Empleando el control de errores, crea una variable llamada datos_csv y carga el archivo CSV dando un cotejamiento de utf-8, agrega un mensaje en caso de que no exista el archivo

try:
    datos_csv = pd.read_csv("Datos_Ventas_Tienda.csv", encoding='utf-8')
except FileNotFoundError:
    print("El archivo no existe")
# •3. Muestra la información general del DataFrame utilizando el método adecuado.

print(datos_csv.info())
# •4. Consulta si existen valores nulos y cuántos hay
print(datos_csv.isnull().sum())
# •5. Quita los espacios al inicio, aplica en columna Productos
print(datos_csv["Producto"].str.strip())

# •6.Aplica un método para convertir la primera letra de cada palabra de la oración en mayúsculas, emplea la columna Productos
for producto in datos_csv["Producto"]:
        print(producto.title())


# •7.Verifica si existen valores duplicados en la columna Precio Unitario e imprime el resultado.

print(datos_csv["Precio Unitario"].duplicated().sum())

# •8.Investiga para qué sirve el método astype()

#Sirve para cambiar el tipo de datos (cast) de una columna (Series) o de un 
# DataFrame entero a otro tipo específico (como pasar de texto a números, o de números enteros a decimales).

# •9.Investiga para que sirve el método to_datetime()
#  Sirve para convertir varios tipos de datos (como texto, números, listas o columnas de un DataFrame) 
# en objetos de tipo fecha y hora (formato datetime64 o Timestamp).


#IMPRIMIR DATOS
#print(datos_csv.shape)