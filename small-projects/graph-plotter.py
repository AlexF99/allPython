###this app will make a graph of any given function, which is input from the user, but it needs improvement, because it requires de user to use x as the variable in the function, besides, it doesn't know what to do if the input is anything else besides a function.

#################################################################

from matplotlib import pyplot as graph

num_elementos = 100

eixo_x = list(range(num_elementos+1))

for n in range(num_elementos+1):
    eixo_x.append(n*-1)

del(eixo_x[len(eixo_x)//2])

eixo_x.sort()

eixo_y = []


# graph.plot e graph.show


funcao = input("funcao a ser avaliada (use x como sua variável): ")

def func(x):
    fdex = eval(funcao)
    return fdex



def f(x):
    f = func(x)
    return f

for x in eixo_x:
    eixo_y.append(f(x))

# tabela de valores

print("Valores:\nX\t|\tY")

for val in range(len(eixo_x)):
    print(eixo_x[val], "\t|\t", eixo_y[val])


# grafico

graph.plot(eixo_x, eixo_y)
graph.grid(1)
graph.xlabel("eixo X")
graph.ylabel("eixo Y")

graph.show()