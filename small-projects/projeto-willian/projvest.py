file_turma1 = open("inputs_1.txt")
file_turma2 = open("inputs_2.txt")
gabarito = open("gabaritos.txt")

gabarito_1 = gabarito.readlines(1)
gabarito_2 = gabarito.readlines(2)


# organizando os gabaritos especiais que serao comparados com os alunos de cada materia aluno [materiasafim, restomaterias]

gab_exa = [gabarito_1[0][:30], gabarito_1[0][30:69]]
gab_lin = [gabarito_1[0][40:69], gabarito_1[0][:40]]
gab_soc = [gabarito_1[0][:10] + gabarito_1[0][50:69], gabarito_1[0][10:50]]
gab_bio = [gabarito_1[0][20:40] + gabarito_1[0][50:60], gabarito_1[0][:20] + gabarito_1[0][40:50] + gabarito_1[0][60:69]]



turma1 = file_turma1.readlines()
len_antes1 = len(turma1)

for lines in range(len(turma1)):
    turma1.append(turma1[lines].split(";"))

del(turma1[:len_antes1])

lista_classif = []


#classificando alunos pelo numero de questoes que acertaram [numdecertas, materia, nome]

for lines in range(len(turma1)):
    questoes_certas = 0
    for qs in range(69):
        if(turma1[lines][2][qs] == gabarito_1[0][qs]):
            questoes_certas += 1
    lista_classif.append([questoes_certas, turma1[lines][1], turma1[lines][0]])

#lista_classif.sort(reverse=True)


print("\n\n\n")
#turma1 = [nome, materia, gabarito]



resp_exatas = []
resp_lin = []
resp_soc = []
resp_bio = []
result_geral = []

#for que extrai as respostas de cada aluno com suas respectivas materias afins separadas [nome, gabmataf, restogab]

for x in range(len(turma1)): # x de 0 a 45


    #exatas

    q_afim = 0 # zera numero de questoes de materias afim
    if (turma1[x][1] == 'EXA'): # verifica se a materia afim do cara é exata
        resp_exatas.append([turma1[x][0], turma1[x][2][:30], turma1[x][2][30:69], "EXA"])


    #linguagens

    if (turma1[x][1] == 'LIN'):
        resp_lin.append([turma1[x][0], turma1[x][2][40:69], turma1[x][2][:40], "LIN"])

    #sociais

    if (turma1[x][1] == 'SOC'):
        resp_soc.append([turma1[x][0], turma1[x][2][:10]+turma1[x][2][50:69], turma1[x][2][10:50], "SOC"])

    #bio

    if (turma1[x][1] == 'BIO'):
        resp_bio.append([turma1[x][0], turma1[x][2][20:40]+turma1[x][2][50:60], turma1[x][2][:20] + turma1[x][2][40:50] + turma1[x][2][60:69], "BIO"])


#agora temos respostas dos alunos separadas e gabaritos separados






def resultado_aluno(resps, gabs):
    for aluno in range(len(resps)):
        afim = 0
        resto = 0
        for qs in range(len(resps[0][1])):
            if resps[aluno][1][qs] == gabs[0][qs]:
                afim += 1
        for qs in range(len(resps[0][2])):
            if resps[aluno][2][qs] == gabs[1][qs]:
                resto += 1
        desempenho_aluno = (7/3)*afim + (4/3)*resto
        acertos_aluno = afim+resto
        print(resps[aluno][0], "; questoes certas: ", acertos_aluno, ";\tdesempenho: %.1f" %desempenho_aluno)









# lista de gabaritos e respostas

lista_geral = [[resp_soc, gab_soc], [resp_lin, gab_lin], [resp_exatas, gab_exa], [resp_bio, gab_bio]]



def resultado_geral(listageral):
    for area in range(len(listageral)):
        for aluno in range(len(listageral[area][0])):
            afim = 0
            resto = 0
            for qs in range(len(listageral[area][0][0][1])):
                if listageral[area][0][aluno][1][qs] == listageral[area][1][0][qs]:
                    afim += 1
            for qs in range(len(listageral[area][0][0][2])):
                if listageral[area][0][aluno][2][qs] == listageral[area][1][1][qs]:
                    resto += 1
            desempenho_aluno = (7/3)*afim + (4/3)*resto
            acertos_aluno = afim+resto
            result_geral.append([listageral[area][0][aluno][0], desempenho_aluno, acertos_aluno, listageral[area][0][0][3]])
    return result_geral





def escolhe_materia():
    print("\n\nsociais - digite 'SOC'")
    print("exatas - digite 'EXA'")
    print("biologicas - digite 'BIO'")
    print("linguagens - digite 'LIN'\n")
    print("exibir todas - digite 'ALL'")
    opcao = input("voce gostaria de ver o resultado dos alunos de qual AREA? ")
    print("\n\n")
    exibe_materia(opcao)




def exibe_materia(opcao):
    if opcao == "SOC":
        resultado_aluno(resp_soc, gab_soc)

    elif opcao == "LIN":
        resultado_aluno(resp_lin, gab_lin)

    elif opcao == "EXA":
        resultado_aluno(resp_exatas, gab_exa)

    elif opcao == "BIO":
        resultado_aluno(resp_bio, gab_bio)

    elif opcao == "ALL":
        resultado_aluno(resp_soc, gab_soc)
        resultado_aluno(resp_lin, gab_lin)
        resultado_aluno(resp_exatas, gab_exa)
        resultado_aluno(resp_bio, gab_bio)

    else:
        print("\n\nVoce nao digitou uma area valida!\n")
        escolhe_materia()



#escolhe_materia()
#
#op = input("terminar o programa: digite 'q'")
#
#while(op != 'q'):
#    escolhe_materia()
#    op = input("terminar o programa: digite 'q'")



alista = resultado_geral(lista_geral)

def search_nome():
    nome = input("digite o nome do aluno: ")
    for nomes in range(len(alista)):
        if nome == alista[nomes][0]:
            print(alista[nomes])




def menu():
    print("\n\nvoce pode:\n1-buscar aluno pelo nome\n2-buscar resultados por area\n3-finalizar")
    escolha = input("o que vai fazer?")
    if escolha == '1':
        search_nome()
        menu()
    elif escolha == '2':
        escolhe_materia()
        menu()
    elif escolha == '3':
        pass
    else:
        start()


def start():
    menu()

start()


#TODO DOCUMENTAR