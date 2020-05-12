from majors import *

def compare_majors(major_one, major_two):
    equals = []
    diffs = []

    for course in major_one:
        if course in major_two:
            equals.append(course)
        else:
            diffs.append(course)

    return {'iguais': equals, 'diferentes': diffs}

def myprint(lista):
    for item in lista:
        print(item)

myprint(compare_majors(eng_comp_7, minhas_cursadas)['diferentes'])
# print(len(compare_majors(eng_comp_7, minhas_cursadas)['diferentes']))
