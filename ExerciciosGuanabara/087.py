lista_final = list()
soma_par = 0
soma_terceiro_coluna = 0
maior_valor_segundo_linha = 0
for c in range(0, 3):
    temp = []
    for x in range(0, 3):
        valor = int(input(f"Digite um valor para [{c}, {x}]: "))
        if valor % 2 == 0:
            soma_par += valor
        if x == 2:
            soma_terceiro_coluna += valor
        if c == 1:
            if valor > maior_valor_segundo_linha:
                maior_valor_segundo_linha = valor
        temp.append(valor)
    lista_final.append(temp)

print("-="*40)

for valor in lista_final:
    for c in range(0, 3):
        print(f"[{valor[c]:^5}]", end="")
    print()
print("-="*40)

print(f"A soma dos valores pares é {soma_par}")
print(f"A soma dos valores da terceira coluna {soma_terceiro_coluna}")
print(f"O muir valor da segunda linha {maior_valor_segundo_linha}")