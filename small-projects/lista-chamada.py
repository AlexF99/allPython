lista = [[12321, 'alexandre', 'freitas'], [2231231, 'julia', 'paganelli'], [3231321, 'isabela', 'freitas'], [42132131, 'marta', 'cris']]
myStudents = []


class Student():
    """docstring for Student."""

    def __init__(self, *info):
        self.firstname = info[1]
        self.lastname = info[2]
        self.__cpf = info[0]
    def get_cpf(self):
        return self.__cpf

class Disciplina():
    """docstring for Disciplina."""

    def __init__(self, nome, *listaObjs):
        self.nome = nome
        self.students = listaObjs

    def get_class_info(self):
        return(self.nome)



for stu in lista:
    myStudents.append(Student(*stu))

# for stuObj in myStudents:
#     print(stuObj.firstname)

math = Disciplina('Matemática', *myStudents)

print(math.nome)
for mathStu in math.students:
    print(mathStu.firstname, mathStu.lastname, mathStu.get_cpf())




# class ClassName():
#     pass
#
#
# t1 = ClassName()
# t2 = ClassName()
# print(t1==t2)
# print(type(t1)==type(t2))
