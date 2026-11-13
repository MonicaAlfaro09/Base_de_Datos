
# PROYECTO 2: IMPORTACION DE DATOS A SQL SERVER
# MONICA FERNANDA ALFARO RANGEL
# DIANA MARITZA MENDOZA COSTILLA

import pandas as pd
import pyodbc
from sqlalchemy import create_engine, URL
from sqlalchemy.exc import SQLAlchemyError

# 1. CONFIGURAR SERVIDOR Y BASE DE DATOS
servidor = r"localhost\LAB3-EQ20"
base_datos = "rheem"

print("CONTROLADORES DISPONIBLES:")
print(pyodbc.drivers())

# 2. CADENA DE CONEXION
cadena_conexion = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={servidor};"
    f"DATABASE={base_datos};"
    "Trusted_Connection=yes;"
)

# 3. CREAR URL Y MOTOR
url = URL.create(
    "mssql+pyodbc",
    query={"odbc_connect": cadena_conexion}
)

motor = create_engine(url)

try:

    # 4. LEER LOS ARCHIVOS LIMPIOS
    df_prod = pd.read_csv(
        "productos_limpios.csv",
        encoding="utf-8-sig"
    )

    df_prov = pd.read_csv(
        "proveedores_limpios.csv",
        encoding="utf-8-sig",
        dtype={"telefono": "string", "correo": "string"}
    )

    df_inv = pd.read_csv(
        "inventarios_limpios.csv",
        encoding="utf-8-sig"
    )

    print("\nARCHIVOS CSV LEIDOS CORRECTAMENTE")

    # 5. VERIFICAR PROVEEDORES
    # NO IMPORTAR REGISTROS CON CAMPOS OBLIGATORIOS VACIOS

    df_prov["telefono"] = (
        df_prov["telefono"]
        .str.replace(r"\D", "", regex=True)
    )

    proveedores_invalidos = df_prov[
        df_prov["telefono"].isna()
        | (df_prov["telefono"] == "")
        | df_prov["correo"].isna()
        | (df_prov["correo"].str.strip() == "")
    ]

    print("\nPROVEEDORES EXCLUIDOS:")
    print(proveedores_invalidos[["id_proveedor", "nombre"]])

    df_prov = df_prov.drop(proveedores_invalidos.index)

    # 6. VERIFICAR RELACION PRODUCTOS-INVENTARIOS
    ids_productos = set(df_prod["id_producto"])

    ids_inventarios = set(df_inv["id_producto"])

    if not ids_inventarios.issubset(ids_productos):
        raise ValueError(
            "Existen inventarios con productos inexistentes."
        )

    # 7. CONECTAR CON SQL SERVER
    with motor.begin() as conexion:

        print("\nCONEXION EXITOSA CON SQL SERVER")

        # 8. COMPROBAR QUE LAS TABLAS ESTEN VACIAS
        tablas = ["Productos", "Proveedores", "Inventarios"]

        for tabla in tablas:
            total = conexion.exec_driver_sql(
                f"SELECT COUNT(*) FROM dbo.{tabla}"
            ).scalar_one()

            if total > 0:
                raise ValueError(
                    f"La tabla {tabla} ya contiene registros. "
                    "Se cancelo la importacion para evitar duplicados."
                )

        # 9. FUNCION PARA INSERTAR CONSERVANDO LOS IDENTITY
        def importar_tabla(df, tabla):

            conexion.exec_driver_sql(
                f"SET IDENTITY_INSERT dbo.{tabla} ON"
            )

            try:
                df.to_sql(
                    tabla,
                    con=conexion,
                    schema="dbo",
                    if_exists="append",
                    index=False
                )
            finally:
                conexion.exec_driver_sql(
                    f"SET IDENTITY_INSERT dbo.{tabla} OFF"
                )

            print(
                f"{tabla}: {len(df)} registros importados correctamente."
            )

        # 10. IMPORTAR PRODUCTOS
        importar_tabla(df_prod, "Productos")

        # 11. IMPORTAR PROVEEDORES
        importar_tabla(df_prov, "Proveedores")

        # 12. IMPORTAR INVENTARIOS
        importar_tabla(df_inv, "Inventarios")

        print("\nIMPORTACION FINALIZADA EXITOSAMENTE")

except FileNotFoundError as error:
    print("No se encontro el archivo:", error.filename)

except (SQLAlchemyError, ValueError) as error:
    print("ERROR DURANTE LA IMPORTACION:", error)

except Exception as error:
    print("ERROR:", error)

finally:
    motor.dispose()
