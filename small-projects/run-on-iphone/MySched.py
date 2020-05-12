#this is an app I am coding for my iphone


# essa parte sera excluida quando o app for mobile
hist_file = open("historico-escolar.txt")

historico = hist_file.readlines()

len_antes = len(historico)

for disciplina in range(len(historico)):
    historico[disciplina] = historico[disciplina][:len(historico[disciplina])-1] #retira os \n do final das strings
    historico.append(historico[disciplina].split('\t'))

del(historico[:len_antes]) # historico no formato [materia, credito, nota]


# informacoes das materias cursadas/em andamento no periodo atual
classes_info = {

    "contab": {"dia1": {"dia": "segunda", "horario": "14:40 - 16:40", "sala": "E-205"},
               "dia2": {"dia": "quarta", "horario": "17:50 - 19:30", "sala": "E-205"},
               "notas": [[8.1, 1], [9.2, 2], [7.4, 3]], # notacao = [nota, peso]
               "professor": "Luci Ines Basseto",
               "nome": "Contabilidade e Gestão de Custos"
    },


    "fisica":  {"dia1": {"dia": "segunda", "horario": "16:40 - 18:40", "sala": "E-108"},
                "dia2": {"dia": "quarta", "horario": "15:50 - 17:30", "sala": "E-201"},
                "notas": [[8.1, 1], [9.2, 2], [7.4, 3]],
                "professor": "Cristovao",
                "nome": "Física Teórica 3"

    },


    "mec2": {"dia1": {"dia": "quinta", "horario": "20:20 - 22:10", "sala": "EB-209"},
             "dia2": {"dia": "sexta", "horario": "19:30 - 21:10", "sala": "EB-209"},
             "notas": [[8.1, 1], [9.2, 2], [7.4, 3]],
             "professor": "Beghetto",
             "nome": "Mecânica Geral 2"

    },


    "resmat": {"dia1": {"dia": "quinta", "horario": "15:50 - 17:30", "sala": "EB-301"},
               "dia2": {"dia": "sexta", "horario": "15:50 - 17:30", "sala": "EB-209"},
               "notas": [[8.1, 1], [9.2, 2], [7.4, 3]],
               "professor": "Alberti",
               "nome": "Resistência dos Materiais 1"
    },


    "hidro": {"dia1": {"dia": "terca", "horario": "18:40 - 21:10", "sala": "EB-302"},
              "dia2": {"dia": "   ", "horario": "", "sala": ""},
              "notas": [[8.1, 1], [9.2, 2], [7.4, 3]],
              "professor": "Moro",
              "nome": "Hidrologia"
    },


    "metodos": {"dia1": {"dia": "terca", "horario": "15:50 - 17:30", "sala": "EB-202"},
                "dia2": {"dia": "sexta", "horario": "13:50 - 15:50", "sala": "EB-202"},
                "notas": [[8.1, 1], [9.2, 2], [7.4, 3]],
                "professor": "Puppi",
                "nome": "Métodos Numéricos Aplicados à Engenharia Civil"
    }
}



# general functions

def search_day(day):
    for materia in classes_info:
        if day in classes_info[materia]["dia1"]["dia"]:
            print(materia, classes_info[materia]["dia1"]["horario"], classes_info[materia]["dia1"]["sala"])
        elif day in classes_info[materia]["dia2"]["dia"]:
            print(materia, classes_info[materia]["dia2"]["horario"], classes_info[materia]["dia2"]["sala"])


def search_class(nome_materia):
    for materia in classes_info:
        if nome_materia in materia:
            print(materia, "- Professor:", classes_info[materia]["professor"])



def calculo_media(input_materia):
    mults = 0
    pesos = 0
    #acessando a materia p calc nota:
    for mat in classes_info:
        if input_materia in mat:
            for nota in range(len(classes_info[mat]["notas"])):
                mults += classes_info[mat]["notas"][nota][0]*classes_info[mat]["notas"][nota][1]
                pesos += classes_info[mat]["notas"][nota][1]
            media = mults/pesos
            print("Média parcial: %.2f" %media)



def coeficiente(historico):
    mults = 0
    creds = 0
    for materia in historico:
        mults += float(materia[1])*float(materia[2])
        creds += float(materia[1])
    result = mults/creds
    print("CR: %.3f" %result)



def imprime_todas():
    for materia in classes_info:
        print(classes_info[materia]["nome"])



def menu(op):
    if op == "1":
        search_day(input("digite um dia da semana: "))
    elif op == "2":
        search_class(input("digite o nome de uma materia: "))
    elif op == "3":
        calculo_media(input("digite o nome da materia: "))
    elif op == "4":
        coeficiente(historico)
    elif op == "5":
        imprime_todas()
    elif op == "6":
        quit()
    start()

def start():
    opcao = input("\n\n\nUTFPR\n\n1 - Pesquisar dia da semana\n2 - Pesquisar materia\n3 - calcular media materia\n"
                  "4 - coeficiente de rendimento\n5 - Materias matriculadas\n6 - Sair\n\n")
    menu(opcao)


start()