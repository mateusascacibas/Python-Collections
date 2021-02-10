vet = list(range(10))
cont = 0

while cont < len(vet):
    vet[cont] = int(input("Digite um numero: "))

    if vet[cont] < 0:
        vet[cont] = 0
    cont += 1

print(vet)