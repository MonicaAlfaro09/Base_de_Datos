#MONICA FERNANDA ALFARO RANGEL



productos =[ "Teclado", "Mouse", "Monitor", "Mouse", "Memoria USB"]
#1. SOLICITAR NOMBRE DEL EMPLEADO
nombre_emp = input ("Escribe el nombre del empleado: ")

#2. SALUDARLO
print("Bienvenido " + nombre_emp)

#3. Agregar un valor vacio
productos.append(" ")

#4.Muestre el segundo producto registrado
print("El segundo producto registrado es: " + productos[1])

#5.Muestre el ultimo producto registrado
print(f"El ultimo producto registrado es: {productos[-1]}")

#6.Muestre la cantidad total de productos
print("La cantidad total de productos es: " + str(len(productos)))

#7.Elimine los productos repetidos y convierta el resultado en una nueva lista
productos_unicos = list(set(productos))

#8.Elimine el registro vacío de la nueva lista
productos_unicos.remove(" ")

#9.Ordene alfabéticamente los productos de la nueva lista
productos_unicos.sort()

#10.Recorra la nuevalista, imprima cada producto y emplea la función title
for producto in productos_unicos:
    print(producto.title())
