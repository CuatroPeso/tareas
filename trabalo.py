import random
kino=True
list_num = []
for a in range(5):
    num_real=random.randint(1, 49)
    list_num.append(num_real)
list_numfavs = []
while kino:
    for b in range(5):
        while True:
            try:
                numfav = int(input("Escoja sus numeros favoritos entre 1 y 49: "))
                if 1 <= numfav <= 49:
                    break
                print("Por favor ingrese un número válido entre 1 y 49.")
            except ValueError:
                print("tamalo master")
        list_numfavs.append(numfav)
    if numfav>=49:
        print("Por favor lea bien las instrucciones")
    else:
        kino=False
        print("Sus numeros favoritos fueron",list_numfavs)
        print("Los numeros para acertar fueron",list_num)
        cuea = 0
        for numfav in list_numfavs:
            if numfav in list_num:
                cuea = cuea+1
        if cuea == 5:
            print("Wena conchetumare te sacaste el kino")
        else:
            print("No hay kino para ti!>:c")
