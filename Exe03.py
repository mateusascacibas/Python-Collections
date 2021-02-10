import numpy as np

vet = list(range(10))

cont = 0
cont2 = 0

while cont < 10:

    vet[cont] = float(input("Digite um valor: "))
    cont += 1


print("Vetor 1: " + format(vet))
print("Vetor ao Quadrado: ", np.square(vet))


