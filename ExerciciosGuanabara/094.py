from operator import truediv

lista_pessoas = list()
media_idade = 0
mulhes = []
continuar = True
while continuar:
    dados_pessoal = {}
    dados_pessoal['nome'] = str(input("Nome: "))
    while True:
        dados_pessoal['sexo'] = str(input("Sexo [M/F]: "))
        if dados_pessoal['sexo'] in 'MmFf':
            break
        else:
            print("Deve apenas Digitar M ou F")
    dados_pessoal['idade'] = int(input("Idade: "))
    media_idade += dados_pessoal['idade']
    lista_pessoas.append(dados_pessoal)
    if dados_pessoal['sexo'] in 'Ff':
        mulhes.append(dados_pessoal['nome'])
    while True:
        parar = str(input("Deseja continuar? [S/N]"))
        if parar =='N' or parar == 'n':
            continuar = False
            break
        elif parar in 'Ss':
            break
        else:
            print("A sua resposta deve ser S ou N")

media = media_idade / len(lista_pessoas)
print("-="*20)
print(f"A) Ao todo temos {len(lista_pessoas)} pessoas cadastradas.")
print(f"B) A média de idade é de {media}")
print(f"C) As mulheres cadastradas foram {mulhes}")
print(f"D) Lista das pessoas que estao acima da media: ")
for pessoa in lista_pessoas:
    if pessoa['idade'] > media:
        print(f"    nome={pessoa['nome']}; sexo={pessoa['sexo']} ; idade={pessoa['idade']}")
