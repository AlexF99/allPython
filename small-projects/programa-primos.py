# programa que identifica numeros primos em um intervalo determinado pelo usuario

print("\n\nDigite o primeiro e ultimo numeros de uma lista para que \nse verifique se cada um deles eh primo\n\n\n")


inicio = int(input("inicio lista: "))
fim = int(input("fim lista: "))

for x in range(inicio, fim+1):
    i = 0
    for aux in range(1, inicio):
        if(inicio % aux == 0):
            i += 1

    if(i == 1):
        print(inicio)

    if (inicio < fim+1):
        inicio += 1
    else:
        break


