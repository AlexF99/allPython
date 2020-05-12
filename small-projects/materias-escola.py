# materias escola

materias = []
op = ''


def adc_materia(new_class_name, new_class_grade):
    new_class_status = [new_class_name, new_class_grade]
    materias.append(new_class_status)

def imprime_boletim():
    print("BOLETIM:")
    for x in range(len(materias)):
        print(materias[x][0], "-", materias[x][1])

def calculo_media():
    notas = 0
    for x in range(len(materias)):
        notas += materias[x][1]
    media = notas/len(materias)
    return media


while (op != 'q'):
    new_class_name = input("nome da materia: ")
    new_class_grade = float(input("nota na materia: "))
    adc_materia(new_class_name, new_class_grade)
    op = input("\n\nparar o app: 'q':\t")

imprimir = input("\n\nimprimir boletim? (s/n):\t")

if (imprimir == 's'):
    imprime_boletim()
    print("\n\nmedia:", calculo_media())

