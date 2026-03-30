from random import randint

valor_sorteado = (randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10))
valores_ordenados = sorted(valor_sorteado)

print(f"Os valores sorteados foram:",end=" ")
for valor in valores_ordenados:
    print(valor,end=" ")


print(f"\nO maior valor sorteado foi: {valores_ordenados[-1]}")
print(f"O menor valor sorteado foi: {valores_ordenados[0]}")