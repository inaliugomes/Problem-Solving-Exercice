from random import sample
from time import sleep
print("-="*20)
print(f"{' '*10}JOGA NA MEGA SENA")
print("-="*20)

sorteio = int(input("Quantos jogos deseja sortear? "))

print(f"{"-="*20} SORTEANDO {sorteio} JOGOS {"-="*20}")
for _ in range(sorteio):
    numero = sorted(sample(range(0, 61), k=6))
    print(numero)
    sleep(1)

print(f"{"-="*20} < BOA SORTE! > {"-="*20}")
