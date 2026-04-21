from random import randint
def sortear():
    return randint(1,10)

lista_numeros = [sortear(),sortear(),sortear(),sortear(),sortear()]

print(f"Sorteando 5 valores da lista: {lista_numeros}")

total = sum(x for x in lista_numeros if x % 2 == 0)

print(f"Somando os valores pares de {lista_numeros}, temos {total}")