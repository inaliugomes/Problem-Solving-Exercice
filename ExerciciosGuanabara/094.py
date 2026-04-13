from operator import truediv

lista_pessoas = list()
media_idade = 0
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
    while True:
        parar = str(input("Deseja continuar? [S/N]"))
        if parar =='N' or parar == 'n':
            continuar = False
            break
        elif parar in 'Ss':
            break
        else:
            print("A sua resposta deve ser S ou N")