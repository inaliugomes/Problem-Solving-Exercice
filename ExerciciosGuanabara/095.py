lista_jogadores = []

continuar = 'S'

while continuar == 'S':
    jogador = {}
    jogador['nome'] = str(input("Nome: "))
    numero_jogo = int(input(f"Quantos jogas jogou {jogador['nome']}: "))
    golos = []
    for c in range(0,numero_jogo):
        golo = int(input(f"Quantos golos marcou na partida {c+1}: "))
        golos.append(golo)
    jogador['golos'] = golos
    lista_jogadores.append(jogador)
    continuar = str(input("Quer continuar? [S/N] ")).upper()
    if continuar == 'N':
        break

print(lista_jogadores)

