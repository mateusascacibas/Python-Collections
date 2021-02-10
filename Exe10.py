vet = list(range(15))
cont = 0

while cont < 15:
    vet[cont] = float(input("Digite um valor: "))
    cont = 1 + cont

media = (sum(vet)) / 15
print(media)