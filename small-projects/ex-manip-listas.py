# exemplo manipulaçao de listas com as funcoes

pontuacao_reversa = [['alexandre', 6.8], ['joao', 7.6], ['guilherme', 4.8], ['leonardo', 5.2], ['julia', 8.9], ['marcelo', 6.7]]

num_vagas = 2

print(pontuacao_reversa)

for x in range(len(pontuacao_reversa)):
    (pontuacao_reversa[x][0], pontuacao_reversa[x][1]) = (pontuacao_reversa[x][1], pontuacao_reversa[x][0])

print('\n\n\n')
pontuacao_reversa.sort(reverse=True)
for x in range(len(pontuacao_reversa)):
    if (x <= num_vagas-1):
        print(x+1, 'lugar: ', pontuacao_reversa[x][1], pontuacao_reversa[x][0], '\tAPROVADO')
    else:
        print(x+1, 'lugar: ', pontuacao_reversa[x][1], pontuacao_reversa[x][0], '\tREPROVADO')

