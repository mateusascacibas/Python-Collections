A = [1,0,5,-2,-5,7]
cont = 0
soma = sum(A)

print("A soma do Array é: " + format(soma))

A[4] = 100

while cont < len(A):
    print(A[cont])
    cont += 1
