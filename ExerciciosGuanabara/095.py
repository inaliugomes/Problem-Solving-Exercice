from operator import truediv

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


print("-="*20)
print(f"{'Cod':<6} {'Nome':<15} {'Gols':<20}{'Total':<6}")
print("-"*47)
for c in range(0,len(lista_jogadores)):
    total_golo = sum(lista_jogadores[c]['golos'])
    gols_str = str(lista_jogadores[c]['golos'])
    print(f"{c:<6} {lista_jogadores[c]['nome']:<15} {gols_str:<20} {total_golo:<6}")


while True:

    jogador = int(input(" Mostrar dados de qual jogador ? (999 para parar): )"))
    if jogador == 999:
        break
    if jogador <= len(lista_jogadores):
        print(f"LEVANTAMENTO DO JOGADOR {lista_jogadores[jogador]['nome']}: ")
        for c,p in enumerate(lista_jogadores[jogador]['golos']):
            print(f"No jogo {c+1} fez {p} gols")

    else:
        print(f"ERRO! Nao existe jogador com codigo {jogador}")
