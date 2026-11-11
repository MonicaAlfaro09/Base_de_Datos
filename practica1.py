#MONICA FERNANDA ALFARO RANGEL

#3
nombre = input ("Escribe su nombre")
print ("Hola " + nombre)

#4
lista = ["Chucky", "Anabelle", "Chucky"]

#5
#append es una funcion que sirve para agregar un elemento a la lista
lista.append(" ")

#6
#SOLO LISTA UN ELEMENTO DE LA LISTA
print(lista[0])

#7
#recorre la lista empleando for
for pelicula in lista:
    print(pelicula)

#8
#CUANTOS ELEMENTOS HAY EN LA LISTA
print("Cantidad de peliculas " + str(len(lista)))

#9
#para que sirve set: para eliminar elementos duplicados de una lista
lista = list(set(lista))

#10
#elimina 

peliculas_unicas = list(set(lista))

print("Peliculas unicas: ")
#11
for peliculas_unicas in peliculas_unicas:
    print(peliculas_unicas)

#12 Repite el paso 10 pero con la nueva lista
    nueva_lista = list(set(lista))

    #13 REMOVE
    lista.remove(" ") 
#14 ordenar
    lista.sort()
#15 imprime la nueva lista
    print(lista)