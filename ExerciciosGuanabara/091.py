from operator import itemgetter
from random import randint
lista_jogadores = list()


for c in range(0, 4):
    todos_jogadores = dict()
    jogador = randint(1, 6)
    todos_jogadores[f'jogador'] = jogador
    lista_jogadores.append(todos_jogadores)
    print(f"O jogador{c} tirou {jogador} no dado")

sorted(lista_jogadores, key=itemgetter('jogador'))
print("-="*15)
print(f"== RANKING DOS JOGADORES ==")

for jogar in lista_jogadores:
    print(jogar['jogador'])


