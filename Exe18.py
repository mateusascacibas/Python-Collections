vet = list(range(10))
cont = 1
num = int(input("Digite um numero: "))
while(cont <= 10):
    vet[cont-1] = num * cont
    cont += 1

print(vet)
