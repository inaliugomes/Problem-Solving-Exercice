lista_persona = [ ]
finalizar = False
maior_peso = 0
menor_peso = 0
nome_maior_peso = []
nome_menor_peso = []
while not finalizar:
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    dados = [nome, peso]
    lista_persona.append(dados)
    continuar = str(input("Continuar? [S/N]")).upper()
    if continuar == "N":
        finalizar = True

for c in range(0, len(lista_persona)):
    print(lista_persona[c])
    if c == 0:
        maior_peso = lista_persona[c][1]
        menor_peso = lista_persona[c][1]
    else:
        if lista_persona[c][1] > maior_peso:
            maior_peso = lista_persona[c][1]
        if lista_persona[c][1] < menor_peso:
            menor_peso = lista_persona[c][1]

for pessoa in lista_persona:
    if pessoa[1] == maior_peso:
        nome_maior_peso.append(pessoa[0])
    if pessoa[1] == menor_peso:
        nome_menor_peso.append(pessoa[0])

print(f"Ao todo, foi registrado {len(lista_persona)} pessoas")
print(f"O maior peso foi de {maior_peso} Kg. Peso de {nome_maior_peso}")
print(f"O menor peso foi de {menor_peso} Kg. Peso de {nome_menor_peso}")

