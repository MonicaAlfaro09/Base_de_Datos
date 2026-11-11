#PROYECTO 2: INTEGRANTES 
#MONICA FERNANDA ALFARO RANGEL Y DIANA MARITZA MENDOZA COSTILLA



import csv
import re
from collections import Counter

try:
    with open("proveedores.csv", "r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        registros = list(lector)
        columnas = lector.fieldnames

    if not registros:
        raise ValueError("El archivo de proveedores está vacío.")

    nombres = [
        r.get("nombre", "").strip().lower()
        for r in registros
        if r.get("nombre", "").strip()
    ]
    repetidos = {
        nombre for nombre, cantidad in Counter(nombres).items()
        if cantidad > 1
    }

    aptos = 0
    no_aptos = 0

    print("REVISIÓN DE PROVEEDORES")
    print("Total de registros:", len(registros))
    print("Columnas:", columnas)

    for numero, registro in enumerate(registros, start=2):
        errores = []

        nombre = registro.get("nombre", "").strip()
        telefono = registro.get("telefono", "").strip()
        correo = registro.get("correo", "").strip()

        if not nombre:
            errores.append("Nombre vacío")
        elif nombre.lower() in repetidos:
            errores.append("Nombre duplicado")

        if not re.fullmatch(r"\d{10}", telefono):
            errores.append("Teléfono inválido")

        patron_correo = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        if not re.fullmatch(patron_correo, correo):
            errores.append("Correo electrónico inválido")

        if errores:
            no_aptos += 1
            print(f"Fila {numero}: NO APTA -> {', '.join(errores)}")
        else:
            aptos += 1

    total = len(registros)
    print("\nRESUMEN")
    print("Registros aptos:", aptos)
    print("Registros no aptos:", no_aptos)
    print(f"Porcentaje apto: {aptos / total * 100:.2f}%")
    print(f"Porcentaje no apto: {no_aptos / total * 100:.2f}%")

except FileNotFoundError:
    print("Error: no se encontró proveedores.csv.")
except (PermissionError, OSError) as error:
    print("Error al leer el archivo:", error)
except (csv.Error, ValueError) as error:
    print("No fue posible analizar el archivo:", error)
