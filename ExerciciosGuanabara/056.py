media = 0
homem_velho = 0
numero_mulher = 0
nome_homem_velho = ''

for c in range(1, 5):
    print(f"---- {c} PESSOA----")
    nome = str(input(f"Nome: "))
    idade = int(input(f"Idade: "))
    sexo = str(input(f"Sexo [M/F]: "))
    media += idade
    if sexo.upper() == "M":
        if idade > homem_velho:
            homem_velho = idade
            nome_homem_velho = nome

    if sexo.upper() == "F" and idade < 20:
        numero_mulher += 1

media = media / 4
print(f"A médida de idade do grupo é de {media} anos.")
print(f"O homem mais velho tem {homem_velho} anos e se chama {nome_homem_velho}.")
print(f"Ao todo sao {numero_mulher} mulheres com menos de 20 anos.")