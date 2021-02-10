vet1 = list(range(10))
vet2 = list(range(10))
vet3 = list(range(10))
cont = 0
i = 0
while cont < 10:
    vet1[cont] = int(input("Digite um numero para o primeiro array: "))
    vet2[cont] = int(input("Digite um numero para o segundo array: "))

    cont += 1
while i < 10:
    if i % 2 == 0:
        vet3[i] = vet1[i]
    else:
        vet3[i] = vet2[i]
    i += 1

print(vet1)
print(vet2)
print(vet3)
