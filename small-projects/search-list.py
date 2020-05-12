# search list

minha_lista = [['alexandre', 'freitas'], ['alexandre', 'oliveira'], ['julia', 'paganelli'], ['andre', 'paganelli']]

def search_list_by_first_name(first_name):
    for x in range(len(minha_lista)):
        if (first_name in minha_lista[x][0]):
            print(minha_lista[x])

def search_list_by_last_name(last_name):
    for x in range(len(minha_lista)):
        if (last_name in minha_lista[x][1]):
            print(minha_lista[x])



print("procurar nome na lista a partir do primeiro nome:")

primeiro_nome = input("digite o primeiro nome: ")

search_list_by_first_name(primeiro_nome)

print(50*'-')

print("procurar nome na lista a partir do sobrenome:")

sobrenome = input("digite o sobrenome: ")

search_list_by_last_name(sobrenome)
