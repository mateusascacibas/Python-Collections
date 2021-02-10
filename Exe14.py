cont = 0
cont_number = 0
i = 0
j = 0
vet = list(range(10))

while cont < 10:
    vet[cont] = int(input("Digite um numero: "))
    cont = cont + 1

while i < 10:
    while j < 10:
        if vet[i] == vet[j]:
            cont_number = cont_number + 1

    print("Numero " + format(vet[i]) + "repetiu " + format(cont_number))
    j = j + 1
i = i + 1

