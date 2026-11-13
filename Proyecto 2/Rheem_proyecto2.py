#PROYECTO 2: INTEGRANTES 
#MONICA FERNANDA ALFARO RANGEL Y DIANA MARITZA MENDOZA COSTILLA

#Crear 3 archivos csv por medio de Python:
import csv
import random
from faker import Faker

fake = Faker("es_MX")
random.seed(42)
Faker.seed(42)

# 1. GENERAR PRODUCTOS


productos = []
nombres_productos = [
    "Aire acondicionado", "Calentador de agua",
    "Termostato", "Minisplit", "Ventilador",
    "Bomba de calor", "Filtro de aire",
    "Control remoto", "Radiador", "Condensador"
]

categorias = [
    "Climatización", "Calefacción",
    "Agua caliente", "Accesorios"
]

for i in range(1, 51):
    productos.append({
        "id_producto": i,
        "nombre": random.choice(nombres_productos) + f" Modelo {i}",
        "categoria": random.choice(categorias),
        "precio": round(random.uniform(500, 15000), 2),
        "activo": random.choice([0, 1])
    })

# Errores intencionales
productos[4] = productos[3].copy()  # Duplicado
productos[9]["precio"] = -250                    # Precio negativo
productos[14]["nombre"] = ""                     # Nombre vacío
productos[19]["precio"] = "precio desconocido"   # Precio inválido
productos[24]["categoria"] = ""                  # Categoría vacía

with open("productos.csv", "w", newline="", encoding="utf-8-sig") as archivo:
    campos = ["id_producto", "nombre", "categoria", "precio", "activo"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(productos)


# 2. GENERAR INVENTARIOS


inventarios = []

for i in range(1, 51):
    inventarios.append({
        "id_inventario": i,
        "id_producto": i,
        "existencia": random.randint(0, 100),
        "ubicacion": f"Almacen {random.randint(1, 5)}"
    })

# Errores intencionales
inventarios[5]["existencia"] = -10
inventarios[9]["ubicacion"] = ""
inventarios[14]["id_producto"] = 999  # producto inexistente
inventarios[19]["existencia"] = "muchas"
inventarios[24] = inventarios[23].copy()  # duplicado

with open("inventarios.csv", "w", newline="", encoding="utf-8-sig") as archivo:
    campos = ["id_inventario", "id_producto", "existencia", "ubicacion"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(inventarios)



# 3. GENERAR PROVEEDORES


proveedores = []

for i in range(1, 51):
    proveedores.append({
        "id_proveedor": i,
        "nombre": fake.company()[:150],
        "telefono": fake.numerify("##########"),
        "correo": fake.email()
    })

# Errores intencionales
proveedores[4] = proveedores[3].copy()  # Duplicado
proveedores[9]["telefono"] = "teléfono incorrecto"
proveedores[14]["correo"] = "correo-sin-formato"
proveedores[19]["nombre"] = ""
proveedores[24]["correo"] = ""

with open("proveedores.csv", "w", newline="", encoding="utf-8-sig") as archivo:
    campos = ["id_proveedor", "nombre", "telefono", "correo"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(proveedores)


print("Archivos CSV creados correctamente.")
print("productos.csv: 50 registros")
print("inventarios.csv: 50 registros")
print("proveedores.csv: 50 registros")
print("Total: 150 registros de ejemplo.")
