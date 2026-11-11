
# MONICA FERNANDA ALFARO RANGEL

# 1. Importar bibliotecas
import pandas as pd
from faker import Faker
from datetime import date

# 2. Configurar Faker
fake = Faker('es_MX')
Faker.seed(4)

# 3. Lista de productos y tipos de movimiento
productos = [
    'Laptop', 'Smartphone', 'Tablet',
    'Smartwatch', 'Auriculares', 'Cámara'
]

tipos_movimiento = ['Entrada', 'Salida']

# 4. Generar 50 movimientos comerciales
registros = []

fecha_inicio = date(2026, 1, 1)
fecha_final = date(2026, 9, 30)

for i in range(50):
    cantidad = fake.random_int(min=1, max=30)

    precio = fake.pydecimal(
        left_digits=4,
        right_digits=2,
        min_value=200,
        max_value=5000
    )

    importe = cantidad * precio

    tipo = fake.random_element(elements=tipos_movimiento)

    # 5. Simular una falla del sistema
    if tipo == "Salida" and cantidad > 15:
        importe = importe + 250

    registros.append({
        "id_movimiento": i + 1,
        "responsable": fake.name(),
        "sucursal": fake.state(),
        "producto": fake.random_element(elements=productos),
        "tipo_movimiento": tipo,
        "cantidad": cantidad,
        "precio_unitario": precio,
        "total_registrado": importe,
        "fecha_movimiento": fake.date_between(
            start_date=fecha_inicio,
            end_date=fecha_final
        )
    })

# Mostrar los registros
print(registros)

# 6. Crear DataFrame y guardar CSV
df = pd.DataFrame(registros)

df.to_csv(
    "Movimientos_Originales.csv",
    encoding="utf-8",
    index=False
)
print("\nArchivo Movimientos_Originales.csv creado correctamente.")
print(df.head())

# 5.	Simula una falla del sistema mediante una condición if: cuando un movimiento sea de tipo
#  Salida y su cantidad supere las 15 unidades, el programa deberá agregar incorrectamente $250 
# al importe registrado. Los demás movimientos conservarán su cálculo correcto.


# 6.	Convierte la información generada en un DataFrame y guárdala en un archivo llamado 
# Movimientos_Originales.csv.
print("-------------6-------------")
df = pd.DataFrame(registros)
df.to_csv("Movimientos_Originales.csv", encoding="utf-8", index=False)

print("Archivo Movimientos_Originales.csv creado correctamente.")

# 7.	Carga el archivo CSV generado empleando try-except-else, contemplando la posibilidad de que no exista.
try:
    cargar_archivo = pd.read_csv("Movimientos_Originales.csv", encoding="utf-8")
except FileNotFoundError:
    print ("No existe el archivo")
else:
    print("El archivo si existe")

# 8.	Muestra la estructura general del archivo, sus dimensiones y el tipo de dato de cada columna.
print("-------------8-------------")
print("\n--- Estructura general del archivo (info) ---")
print(cargar_archivo.info())

print("\n--- Dimensiones (filas, columnas) ---")
print(cargar_archivo.shape)

print("\n--- Tipo de dato de cada columna ---")
print(cargar_archivo.dtypes)

# 9.	Comprueba si existen valores nulos o registros completamente duplicados e imprime los
#  resultados, aun cuando no se encuentre ninguno.
print("-------------9-------------")
valores_nulos = cargar_archivo.isnull().sum().sum()
valores_duplicados = cargar_archivo.duplicated().sum()

if (valores_duplicados + valores_nulos) >0:
    print(f"Existen {valores_nulos} valores nulos y {valores_duplicados} valores duplicados")
else:
    print(f"No existen valores nulos ni duplicados: {valores_duplicados}, {valores_nulos}")

# 10.	Crea una nueva columna llamada total_esperado, calculando el valor que debería tener cada 
# movimiento de acuerdo con la cantidad y el precio unitario.

cargar_archivo["total_esperado"] = cargar_archivo["cantidad"] * cargar_archivo["precio_unitario"]
# 11.	Incorpora una columna llamada diferencia que permita conocer cuánto varía el importe
#  registrado respecto al importe esperado.
cargar_archivo["diferencia"] = (cargar_archivo["total_registrado"] - cargar_archivo["total_esperado"])

# 12.	Muestra únicamente los movimientos que presentan diferencias económicas.
print("----------12-------------")
filtro = cargar_archivo[cargar_archivo["diferencia"]!=0]
print(filtro)

# 13.	Calcula el importe total de las diferencias detectadas y determina cuántas operaciones 
# resultaron afectadas.
print("----------------13-------------")
total_diferencias = cargar_archivo["diferencia"].sum()
operaciones_afectadas = (cargar_archivo["diferencia"].round(2) != 0).sum()
print(f"\nImporte total de las diferencias detectadas: ${total_diferencias:,.2f}")
print(f"Número de operaciones afectadas: {operaciones_afectadas}")

# 14.	Normaliza los nombres de los productos eliminando espacios innecesarios y 
# utilizando un mismo formato de mayúsculas y minúsculas.
cargar_archivo["producto"] = cargar_archivo["producto"].str.strip().str.title()

# 15.	Corrige únicamente los importes incorrectos de total_registrado, 
# tomando como referencia los valores de total_esperado.
cargar_archivo.loc[cargar_archivo["diferencia"].round(2) != 0, "total_registrado"] = cargar_archivo["total_esperado"]

# 16.	Cambia el nombre de la columna total_registrado por importe_final.

cargar_archivo = cargar_archivo.rename(columns={"total_registrado": "importe_final"})

# 17.	Genera un nuevo DataFrame que contenga exclusivamente las operaciones de tipo 
# Salida con cantidades superiores a 15 unidades.
df_salidas_altas = cargar_archivo[(cargar_archivo["tipo_movimiento"] == "Salida") & (cargar_archivo["cantidad"] > 15)]
print("\n--- Operaciones de tipo Salida con cantidad superior a 15 ---")
print(df_salidas_altas)

# 18.	Exporta la información corregida a un archivo llamado Movimientos_Corregidos.csv.
print("-------------18-------------")
cargar_archivo.to_csv("Movimientos_Corregidos.csv", encoding="utf-8", index=False)
print("\nArchivo Movimientos_Corregidos.csv exportado correctamente.")