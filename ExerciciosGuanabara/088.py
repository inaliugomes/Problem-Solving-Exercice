from random import randint
from time import sleep
print("-="*20)
print(f"{' '*10}JOGA NA MEGA SENA")
print("-="*20)

sorteio = int(input("Quantos jogos deseja sortear? "))

print(f"{"-="*20} SORTEANDO {sorteio} JOGOS {"-="*20}")
for c in range(0, sorteio):
    numeros_sorteados = []
    for x in range(0, 6):
        numero_aleatorio = randint(1, 60)
        if numero_aleatorio not in numeros_sorteados:
            numeros_sorteados.append(numero_aleatorio)
        else:
            while True:
                numero_aleatorio = randint(1, 60)
                if numero_aleatorio not in numeros_sorteados:
                    numeros_sorteados.append(numero_aleatorio)
                    break

    numeros_sorteados.sort()
    print(numeros_sorteados)
    sleep(1)

print(f"{"-="*20} < BOA SORTE! > {"-="*20}")
