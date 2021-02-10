vet = list(range(20))
cont = 0
cont_2 = 0
apagado = 0
while(cont < 20):

    vet[cont] = int(input("Digite um numero: "))

    while (cont_2 < cont):

        if (vet[cont] == vet[cont_2]):
            vet[cont] = "Repetido"

        cont_2 += 1

    cont += 1
    cont_2 = 0
print(vet)