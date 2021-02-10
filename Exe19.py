vet = list(range(50))
cont = 0

while cont < 50:
    vet[cont] = ((cont + 5) * cont) % (cont + 1)
    cont += 1
print(vet)