#PROYECTO 2: INTEGRANTES 
#MONICA FERNANDA ALFARO RANGEL Y DIANA MARITZA MENDOZA COSTILLA

import csv
from collections import Counter

archivo_csv = "productos.csv"

try:
    with open(archivo_csv, "r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        registros = list(lector)
        columnas = lector.fieldnames

    if not registros:
        raise ValueError("El archivo csv está vacío.")

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

    print("REVISIÓN DE PRODUCTOS")
    print("Total de registros:", len(registros))
    print("Columnas:", columnas)

    for numero, registro in enumerate(registros, start=2):
        errores = []

        nombre = registro.get("nombre", "").strip()
        categoria = registro.get("categoria", "").strip()
        precio = registro.get("precio", "").strip()
        activo = registro.get("activo", "").strip()

        if not nombre:
            errores.append("Nombre vacío")
        elif nombre.lower() in repetidos:
            errores.append("Nombre duplicado")

        if not categoria:
            errores.append("Categoría vacía")

        try:
            valor = float(precio)
            if valor <= 0:
                errores.append("Precio debe ser mayor que cero")
        except (ValueError, TypeError):
            errores.append("Precio no numérico")

        if activo not in ("0", "1"):
            errores.append("Valor de activo inválido")

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
    print(f"Error: no se encontró el archivo {archivo_csv}.")
except (PermissionError, OSError) as error:
    print("Error al leer el archivo:", error)
except (csv.Error, ValueError) as error:
    print("No fue posible analizar el archivo:", error)



