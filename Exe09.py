vet = list(range(6))
cont = 0
cont2 = 5
while cont < 6:
    vet[cont] = float(input("Digite um valor: "))
    cont = 1 + cont

while cont2 >= 0:

    if(vet[cont2] % 2 == 0):
        print(vet[cont2])

    cont2 -= 1