vet = list(range(10))
cont = 0
maior = 0
posicao = 0
while cont < len(vet):
    vet[cont] = int(input("Digite um valor: "))
    if(cont == 0):
        maior = vet[cont]
        posicao = cont
    else:
        if(vet[cont] > maior):
            maior = vet[cont]
            posicao = cont


    cont = cont + 1

print("O maior numero desse conjunto é o " + format(maior) + " e esta na posicao " + format(posicao))
