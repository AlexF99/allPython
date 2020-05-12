from enemdata import *

def calcula_corretas(gabarito, respostas):
    # corretas = 0

    for index in range(len(gabarito)):
        if respostas[index] != gabarito[index]:
            # corretas += 1
            print(str(index + 136) + ' ' + gabarito[index])

    # print(corretas)

calcula_corretas(gabarito2013, respostas2013)
