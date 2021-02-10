import random as rd

vetA = list(range(10))
vetB = list(range(10))
vetC = list(range(10))
cont = 0

while cont < 10:
    vetA[cont] = rd.randint(0,10)
    vetB[cont] = rd.randint(0, 10)
    vetC[cont] = vetA[cont] - vetB[cont]

    cont += 1
print(vetC)