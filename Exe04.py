import numpy as np
import random as rd
vet = list(range(8))
cont = 0

while cont < 8:

    vet[cont] = float(input("Digite um valor: "))
    cont += 1

a = rd.randint(0,7)
a = vet[a]
b = rd.randint(0,7)
b = vet[b]

soma = a + b
print("A soma de " + format(a) + " e " + format(b) + " é " + format(soma))
