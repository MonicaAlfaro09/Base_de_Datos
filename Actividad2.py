#MONICA FERNANDA ALFARO RANGEL


#1.Solicita el nombre del cuidador e imprime un mensaje de bienvenida

nombre_cuidador = input ("Escribe tu nombre: ")
print ("Bienbenid@" + nombre_cuidador + "!")

#2.Crea un diccionario llamado especies que contenga tres especies y la cantidad de ejemplares.
especies = {
    "Leon": 5,
    "Tigre": 3,
    "Elefante": 7,
    "Cebra": 9
}
#3.Agrega la especie Jirafa con una cantidad inicial de 9
especies.setdefault("Jirafa",9)


#4.Actualiza la cantidad de Jirafa a 10 ejemplares.
especies.update({"Jirafa":10})

#5.Recorre el diccionario e imprime el nombre y la cantidad de ejemplares. No olvides usar la función ítems()
for nombre, cantidad in especies.items():
    print(nombre, ":", cantidad)
    print(f"{nombre} : {cantidad}")
    print(nombre + ":" + str(cantidad))

for especies in especies.items():
    print(especies)
#6.Elimina la primera especie registrada en el diccionario.
especies.pop("Leon", 5)

#7.Comprueba si la clave "Jirafa" existe e imprime un mensaje indicando si la especie se encuentra registrada.
if "Jirafa" in especies:
    print("La especie Jirafa esta registrada.")
else:
    print("La especie Jirafa no esta registrada.")

#8.Crea una copia del diccionario.
especies_copia = especies.copy()

#9. Imprime únicamente los valores del diccionario copia.
print("Valores de la copia del diccionario:")
for valor in especies_copia.values():
    print(valor)

#10. Utiliza el método update() para modificar la cantidad de dos especies del diccionario e imprime el resultado.
especies.update({"Tigre":4, "Elefante":8})
print(especies)