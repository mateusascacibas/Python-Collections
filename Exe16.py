vet = list(range(5))
cod = 3
op = 0
while(op < 5):
    vet[op] = int(input("Digite um numero: \n "))
    op += 1


while(cod != 0):
    cod = int(input("Digite 0 para sair \n 1 para mostrar o vetor \n 2 para mostrar ele ao contrario \n"))
    if(cod == 1):
        print(vet)
        print("\n")
    elif(cod == 2):
        print(vet[::-1])
        print("\n")
    else:
        if(cod == 0):
            break
        else:
            print("Opção Invalida.\n")