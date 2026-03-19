maior_peso = 0
menor_peso = 0

for c in range(1,6):
    peso = float(input(f"Peso da {c} pessoa: "))
    if peso > maior_peso:
        maior_peso = peso

    if c == 1:
        menor_peso = peso
    else:
        if peso < menor_peso:
            menor_peso = peso


print(f"O maior peso lido foi de {maior_peso}")
print(f"O menor peso lido foi de {menor_peso}")