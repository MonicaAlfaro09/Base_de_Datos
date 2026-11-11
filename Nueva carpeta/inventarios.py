#PROYECTO 2: INTEGRANTES 
#MONICA FERNANDA ALFARO RANGEL Y DIANA MARITZA MENDOZA COSTILLA


import csv
from collections import Counter

try:
  
    with open("productos.csv", "r", encoding="utf-8-sig", newline="") as archivo:
        productos = list(csv.DictReader(archivo))

    ids_productos = {
        r.get("id_producto", "").strip()
        for r in productos
        if r.get("id_producto", "").strip()
    }

    
    with open("inventarios.csv", "r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        registros = list(lector)
        columnas = lector.fieldnames

    if not registros:
        raise ValueError("El archivo de inventarios está vacío.")

    ids = [
        r.get("id_producto", "").strip()
        for r in registros
        if r.get("id_producto", "").strip()
    ]
    repetidos = {
        valor for valor, cantidad in Counter(ids).items()
        if cantidad > 1
    }

    aptos = 0
    no_aptos = 0

    print("REVISIÓN DE INVENTARIOS")
    print("Total de registros:", len(registros))
    print("Columnas:", columnas)

    for numero, registro in enumerate(registros, start=2):
        errores = []

        id_producto = registro.get("id_producto", "").strip()
        existencia = registro.get("existencia", "").strip()
        ubicacion = registro.get("ubicacion", "").strip()
        id_inventario = registro.get("id_inventario", "").strip()

        if not id_inventario.isdigit() or int(id_inventario) <= 0:
            errores.append("ID de inventario inválido")

        if not id_producto.isdigit() or int(id_producto) <= 0:
            errores.append("ID de producto inválido")
        else:
            if id_producto not in ids_productos:
                errores.append("Producto inexistente en el catálogo")
            if id_producto in repetidos:
                errores.append("Producto repetido en inventarios")

        try:
            cantidad = int(existencia)
            if cantidad < 0:
                errores.append("Existencia negativa")
        except (ValueError, TypeError):
            errores.append("Existencia no numérica o no entera")

        if not ubicacion:
            errores.append("Ubicación vacía")

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

except FileNotFoundError as error:
    print("Error: falta un archivo necesario:", error.filename)
except (PermissionError, OSError) as error:
    print("Error al leer los archivos:", error)
except (csv.Error, ValueError) as error:
    print("No fue posible analizar los datos:", error)
