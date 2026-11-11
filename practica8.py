#MONICA FERNANDA ALFARO RANGEL
import pandas as pd
from faker import Faker
from datetime import date 
# print(pyodbc.drivers())
fake = Faker("es_MX")
Faker.seed(7)
#2 PRODUCTOS

productos = pd.DataFrame({
    "id_producto": [1,2,3,4,5,6],
    "producto":["Teclado","Mouse","Monitor","Memoria USB","Camara web","Audifonos"],
    "precio":[350.00,200.00,3500.00,180.00,750.00,600.00],
}
)
 #3 50 ventas

datos_ventas=[]
fecha_inicio = date(2025,12,30)
fecha_final = date(2026,10,31)
for i in range (0,50):
    id_producto = fake.random_int(min=1, max=6)
    precio = productos [productos ["id_producto"]
                        ==id_producto].iloc[0]

    precio= productos.loc[productos["id_producto"]
                     ==id_producto, "precio"].iloc[0]
    cantidad = fake.random_int(min=1, max=10)

    subtotal = cantidad * precio

    datos_ventas.append({
            "id_ventas": i+1,
            "id_producto": id_producto,
            "precio_unitario":precio,
            "cantidad": cantidad,
            "subtotal": subtotal,
            "fecha_venta": fake.date_between(
                start_date=fecha_inicio, end_date=fecha_final)
    
        })

ventas = pd.DataFrame(datos_ventas)
#solo cambia el signo
ventas.loc[5, "cantidad"] *= -1
ventas.loc[6, "cantidad"]*= -1
#si cambia el valor
ventas.loc[1, "id_producto"] =999
ventas.loc[2, "cantidad"] = -5
ventas.loc[1, "id_producto"] = 8

ventas =pd.concat(
    [
        ventas, ventas.iloc[[10]].copy()],
        ignore_index=True 
)

ventas.to_csv("Ventas_Originales_alfaro.csv", index=False, encoding="utf-8")






