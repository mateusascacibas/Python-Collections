import numpy as np
import random as rd
vet = list(range(10))
vet2 = list(range(10))
cont = 0
cont2= 0

while cont < 10:
    vet[cont] = rd.randint(0,50)
    cont+= 1

while cont2 < 10:
    if (vet[cont2] % 2 != 0):
        vet2[cont2] = vet[cont2]
    else:
        vet2[cont2] = 0
    cont2 += 1

print(vet)
print(vet2)
