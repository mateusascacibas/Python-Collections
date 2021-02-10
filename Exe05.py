vet = list(range(10))
cont = 0
pares = 0
while cont < len(vet):
    vet[cont] = int(input("Digite um valor: "))

    if(vet[cont] % 2 == 0):
        pares += 1

    cont = cont + 1

print("O numero de pares é: " + format(pares))