vet = list(range(5))
cont = 0
maior = 0
menor = 0
while cont < len(vet):
    vet[cont] = int(input("Digite um valor: "))
    if(cont == 0):
        maior = vet[cont]
        menor = vet[cont]
    else:
        if(vet[cont] > maior):
            maior = vet[cont]
        elif(vet[cont] < menor):
            menor = vet[cont]


    cont = cont + 1

media = (sum(vet)) / 5
print("O maior numero desse conjunto é o " + format(maior) + " e o menor é o " + format(menor) + " alem disso, a média geral é: " + format(media))
