
numero_1 = int(input(f"Adicionar o {1} numero:"))
numero_2 = int(input(f"Adicionar o {2} numero:"))
numero_3 = int(input(f"Adicionar o {3} numero:"))
numero_4 = int(input(f"Adicionar o {4} numero:"))
numeros = (numero_1,numero_2,numero_3,numero_4)
par = 0
for p in numeros:
    if p % 2 == 0:
        par += 1

print(f"O numero 9 aparece {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"O numero 3 aprece na {numeros.index(3)+1} posicao")
print(f"Existem {par} numero pares na lista")
