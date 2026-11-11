# 1.	Importa la biblioteca pandas y Faker. Configura Faker para generar datos de México (es_MX).
import pandas as pd
from faker import Faker

fake = Faker('es_MX')

# 2.	Empleando el control de errores, crea una variable llamada datos_csv y carga el archivo CSV, agrega un mensaje en caso de que no exista el archivo y utiliza else para mostrar la información general del DataFrame.
try:
    datos_csv = pd.read_csv("Datos_Ventas_Tienda.csv", encoding='utf-8')
except FileNotFoundError:
    print("El archivo no existe.")
else:
    print("Información general del DataFrame:")
    print(datos_csv.info())

# 3.	Convierte la columna Fecha del archivo CSV al formato día-mes-año
resultado = pd.to_datetime(datos_csv["Fecha"], errors="coerce", 
                           format="%m/%d/%Y").dt.strftime("%d/%m/%Y")
print(resultado)

# 4.	Filtra e imprime los registros del archivo CSV donde el Precio Unitario >500
filtro = datos_csv[datos_csv["Precio Unitario"] > 500]
print(filtro)

# 5.	Investiga el método pydecimal()

# 6.	Genera un número entero aleatorio entre 1 y 100, empleando Faker
numero_aleatorio = fake.random_int(min=1, max=100)

print(numero_aleatorio)

# 7.	Genera una lista llamada cursos que contenga 5 nombres de asignaturas e imprime 2 valores que puedan repetirse.
cursos = ["Matemáticas", "Historia", "Biología", "Física", "Base de datos"] 
print(fake.random_elements(elements=cursos, length=2, unique=False))


# 8.	Renombra la columna Precio Unitario a Precio e imprime los primeros 5 registros
renamed_df = datos_csv.rename(columns={"Precio Unitario": "Precio"})
print("Primeros 5 registros con columna renombrada:")
print(renamed_df.head())

# 9.	 Convierte los valores de la columna Fecha en el formato dd/mm/yyyy
fechas = pd.to_datetime(datos_csv["Fecha"], errors = "coerce").dt.strftime("%d/%m/%Y")
print("FECHAS CONVERTIDAS:")
print(fechas)

# 10.	.Crea una lista vacía llamada datos_exportar
datos_exportar = []

# 11.	 Emplea un ciclo for para generar 15 registros, utilizando diccionarios que deberán contener lo siguiente y emplea el método append() para agregar los datos
for i in range(15):
    registro = {
        "Nombre": fake.first_name(),
        "Apellido": fake.last_name(),
        "Correo": fake.email(),
        "Dirección": fake.address(),
        "Teléfono": fake.phone_number()
    }
    datos_exportar.append(registro)
# 12.	Muestra los registros almacenados en la lista
print(datos_exportar)

# esto lo borras despues 

print(datos_csv.head())

# 9.Convierte los valores de la columna Fecha en el formato dd/mm/yyyy


nombre = "Laxuz"
print("HOLA " + nombre)
print("Bienvenidos a Python")