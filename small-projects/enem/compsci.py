# read tx file
from materiasCS import *

def verPeriodo(per):
    for mat in per:
        if(mat in obrigatorias):
            print(mat + ': ' + obrigatorias[mat])

# print(obrigatorias['CI1055'] + '–>' + obrigatorias['CI1056'] + '–>' + obrigatorias['CI1057'])
# print(obrigatorias['CI1055'] + '->' + obrigatorias['CI1001'] + '–>' + obrigatorias['CI1002'])
# print(obrigatorias['CI1068'] + '–>' + obrigatorias['CI1210'] + '–>' + obrigatorias['CI1212'])
# print(obrigatorias['CM304'] + '–>' + obrigatorias['CI1237'])
# print(obrigatorias['CMA111'] + '–>' + obrigatorias['CMA211'])

for per in periodos:
    print('')
    verPeriodo(per)

# for opt in optativas:
#     print(opt, optativas[opt])
