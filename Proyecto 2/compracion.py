#ALFARO RANGEL MONICA FERNANDA Y MENDOZA COSTILLA DIANA MARITZA 
import pandas as pd

def comparar_archivos(original, limpio, llave, nombre):
    antes = pd.read_csv(original)
    despues = pd.read_csv(limpio)

    # Comprobar registros mediante su llave primaria
    antes = antes.drop_duplicates(subset=[llave], keep="first")
    despues = despues.drop_duplicates(subset=[llave], keep="first")

    ids_antes = set(antes[llave].dropna())
    ids_despues = set(despues[llave].dropna())

    conservados = 0
    corregidos = 0

    # Comparar los registros que permanecieron
    comunes = ids_antes.intersection(ids_despues)

    for identificador in comunes:
        fila_antes = antes[antes[llave] == identificador].iloc[0]
        fila_despues = despues[despues[llave] == identificador].iloc[0]

        if fila_antes.equals(fila_despues):
            conservados += 1
        else:
            corregidos += 1

    descartados = len(ids_antes - ids_despues)

    # Validar registros originales y limpios
    total_antes = len(antes)
    total_despues = len(despues)

    aptos_antes = total_antes - (
        antes.isnull().any(axis=1).sum()
    )
    no_aptos_antes = total_antes - aptos_antes

    aptos_despues = total_despues - (
        despues.isnull().any(axis=1).sum()
    )
    no_aptos_despues = total_despues - aptos_despues

    print("\n================================")
    print("COMPARACIÓN:", nombre)
    print("================================")

    print("Registros originales:", total_antes)
    print("Registros después de limpieza:", total_despues)
    print("Conservados:", conservados)
    print("Corregidos:", corregidos)
    print("Descartados:", descartados)

    print("\nANTES DE LA LIMPIEZA")
    print("Aptos:", aptos_antes)
    print("No aptos:", no_aptos_antes)
    print("Porcentaje aptos:", round(aptos_antes / total_antes * 100, 2), "%")
    print("Porcentaje no aptos:", round(no_aptos_antes / total_antes * 100, 2), "%")

    print("\nDESPUÉS DE LA LIMPIEZA")
    print("Aptos:", aptos_despues)
    print("No aptos:", no_aptos_despues)
    print("Porcentaje aptos:", round(aptos_despues / total_despues * 100, 2), "%")
    print("Porcentaje no aptos:", round(no_aptos_despues / total_despues * 100, 2), "%")


try:
    comparar_archivos(
        "productos.csv",
        "productos_limpios.csv",
        "id_producto",
        "PRODUCTOS"
    )

    comparar_archivos(
        "inventarios.csv",
        "inventarios_limpios.csv",
        "id_inventario",
        "INVENTARIOS"
    )

    comparar_archivos(
        "proveedores.csv",
        "proveedores_limpios.csv",
        "id_proveedor",
        "PROVEEDORES"
    )

except FileNotFoundError as error:
    print("No se encontró uno de los archivos:", error)

except Exception as error:
    print("Ocurrió un error:", error)
