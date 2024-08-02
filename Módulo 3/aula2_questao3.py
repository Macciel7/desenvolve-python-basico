idade_aluno = int(input('Qual a sua idade? '))
idade_adequada = 16 <= idade_aluno <= 18

jogos = input('Você já jogou pelo menos 3 jogos de tabuleiro? (True ou False) ')
jogos_adequados = jogos == 'True'

vitorias = int(input('E quantos jogos você já ganhou? '))
vitorias_adequadas = vitorias > 0

apto = idade_adequada and jogos_adequados and vitorias_adequadas

print ('Apto para ingressar no clube de jogos de tabuleiro:', apto)