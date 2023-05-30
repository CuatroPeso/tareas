import random
kino=True
list_num = [] #Lista de numeros aleatorios
for a in range(5): #El ciclo para crear los numeros
    num_real=random.randint(1, 49) #Creacion de numeros
    list_num.append(num_real) #Agregar numeros a la lista
list_numfavs = [] #Lista numeros del usuario
while kino:
    for b in range(5):#Ciclo para pedir los 5 numeros
        while True:
            try:
                numfav = int(input("Escoja sus numeros favoritos entre 1 y 49: ")) #Se le pide al usuario ingresar un numero entre 1 y 49
                if 1 <= numfav <= 49: #Si el numero es mayor o igual a 1 o menor y igual a 49 entonces el while termina, de lo contrario sigue
                    break
                print("Por favor ingrese un número válido entre 1 y 49.")
            except ValueError:
                print("tamalo master") #En caso de que el usuario no ingrese numero
        list_numfavs.append(numfav) #Se guarda el numero del usuario en la lista "list_numfavs"
    kino=False #Se pone el flag en false para terminar el while
print("Sus numeros favoritos fueron",list_numfavs)
print("Los numeros para acertar fueron",list_num)
cuea = 0 #Contador para ver cuantos numeros acerto el usuario
for numfav in list_numfavs: #Revisa cada numero del usuario
    if numfav in list_num: #Si el numero esta en la lista de numero entonces aumenta el contador
        cuea = cuea+1
        list_num.remove(numfav) #Elimina el numero de la lista random para que no se vuelva a comprobar
if cuea == 5: #Si el contador esta a 5, significa que el usuario acerto a todos lo numeros
    print("Wena te sacaste el kino")
else:
    print("No hay kino para ti!>:c")
