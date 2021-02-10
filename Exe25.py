vet = list(range(100))
cont = 0

while cont < len(vet):
    if(cont % 7 != 0):
        vet[cont] = cont

    cont += 1

print(vet)