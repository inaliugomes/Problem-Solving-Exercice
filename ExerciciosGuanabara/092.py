from datetime import date

current_year = date.today().year

dados = {}
dados["Nome"] = str(input("Nome: "))
idade = int(input("Idade: "))
dados["Idade"] = (current_year - idade)
dados["Carteira"] = int(input("Carteira de trabalho: (0 nao tem): "))


if dados["Carteira"] != 0:
    dados["Ano_contratacao"] = int(input("Ano de contratacao: "))
    dados["Salario"] = int(input("Salario: "))
    dados["oposentar"] = 66 - dados["Idade"]
print("-="*30)


for k, v in dados.items():
    print(f"{k} tem o valor {v}")