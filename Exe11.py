vet = list(range(10))
cont = 0
negativos = 0
soma = 0
while cont < len(vet):
    vet[cont] = float(input("Digite um valor: "))
    if(vet[cont] > 0):
        soma += vet[cont]
    else:
        if(vet[cont] < 0):
            negativos += 1

    cont = cont + 1

print("A soma dos positivos é:  " + format(soma) + " e o numero de negativos é:  " + format(negativos))