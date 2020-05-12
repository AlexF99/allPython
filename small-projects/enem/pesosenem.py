mat = 905.5
nat = 636.5
lin = 610.7
hum = 638
red = 840

def pesos_utf(matematica, naturais, linguagens, humanas, redacao):
    return (matematica*4 + naturais*2 + linguagens + humanas + redacao) / 9

def media_simples(matematica, naturais, linguagens, humanas, redacao):
    return (matematica + naturais + linguagens + humanas + redacao) / 5

def pesos_civilfederal(matematica, naturais, linguagens, humanas, redacao):
    return (matematica*5 + naturais*2 + linguagens*5 + humanas + redacao*2) / 15

def pesos_compscifederal(matematica, naturais, linguagens, humanas, redacao):
    return (matematica*4 + naturais + linguagens + humanas + redacao*2) / 9

def pesos_odontofederal(matematica, naturais, linguagens, humanas, redacao):
    return (matematica + naturais*3 + linguagens*2 + humanas*1 + redacao*5) / 12

def pesos_compUFSC(matematica, naturais, linguagens, humanas, redacao):
    return (matematica*3 + naturais + linguagens + humanas + redacao*2) / 8

def printAll():
    print('eng UTFPR: ' + str(pesos_utf(mat, nat, lin, hum, red)))
    print('civil UFPR: ' + str(pesos_civilfederal(mat, nat, lin, hum, red)))
    print('odonto UFPR: ' + str(pesos_odontofederal(mat, nat, lin, hum, red)))
    print('compsci UFPR: ' + str(pesos_compscifederal(mat, nat, lin, hum, red)))
    print('compsci UFSC: ' + str(pesos_compUFSC(mat, nat, lin, hum, red)))
    print('media_simples: ' + str(media_simples(mat, nat, lin, hum, red)))

printAll()
