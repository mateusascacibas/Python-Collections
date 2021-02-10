vet = list(range(5))
cont = 0
maior = 0
menor = 0
posicao_maior = 0
posicao_menor = 0
while cont < len(vet):
    vet[cont] = int(input("Digite um valor: "))
    if(cont == 0):
        maior = vet[cont]
        menor = vet[cont]
        posicao_maior = 0
        posicao_menor = 0

    else:
        if(vet[cont] > maior):
            maior = vet[cont]
            posicao_maior = cont

        elif(vet[cont] < menor):
            menor = vet[cont]
            posicao_menor = cont


    cont = cont + 1

print("O maior numero desse conjunto esta na posicao " + format(posicao_maior) + " e o menor na posicao " + format(posicao_menor))
