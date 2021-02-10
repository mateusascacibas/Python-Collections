vetAlt = list(range(10))
vetNum= list(range(10))
cont = 0
numeroMaior = 0
alturaMaior = 0
numeroMenor = 0
alturaMenor = 0
while cont < 10:
    vetNum[cont] = float(input("Digite o numero do aluno: "))
    vetAlt[cont] = float(input("Digite a altura: "))

    if cont == 0:
        numeroMaior = vetNum[cont]
        alturaMaior = vetAlt[cont]
        numeroMenor = vetNum[cont]
        alturaMenor = vetAlt[cont]
    else:
        if vetAlt[cont] > alturaMaior:
            numeroMaior = vetNum[cont]
            alturaMaior = vetAlt[cont]
        elif vetAlt[cont] < alturaMenor:
            numeroMenor = vetNum[cont]
            alturaMenor = vetAlt[cont]

    cont += 1

print("O menor tem altura " + format(alturaMenor) + " e é o numero " + format(numeroMenor))
print("O maior tem altura " + format(alturaMaior) + " e é o numero " + format(numeroMaior))
