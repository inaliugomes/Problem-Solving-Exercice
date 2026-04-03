lista_final = list()

for c in range(0, 3):
    temp = []
    for x in range(0, 3):
        valor = int(input(f"Digite um valor para [{c}, {x}]: "))
        temp.append(valor)
    lista_final.append(temp)

print("-="*40)

for valor in lista_final:
    for c in range(0, 3):
        print(f"[{valor[c]:^5}]", end="")
    print()
