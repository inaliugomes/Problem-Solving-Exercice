jogador = {}

jogador['jogador'] = str(input("Nome do Jogador: "))
quantidade = int(input("Quantidade: "))
golos = []

for i in range(quantidade):
    golos.append(int(input(f"Quantos Gols na partida {i}:")))

jogador['gols'] = golos
jogador['total'] = sum(golos)

print("-="*30)
print(jogador)
print("-="*30)

for k , v in jogador.items():
    print(f"{k}: {v}")
print("-="*30)
print(f"O jogador {jogador['jogador']} jogou {len(jogador['gols'])} partidas")


for i in range(len(jogador['gols'])):
    print(f"    => Na partida {i}, fez {jogador['gols'][i]} gols")

print(f"Foi um total de {jogador['total']} gols")