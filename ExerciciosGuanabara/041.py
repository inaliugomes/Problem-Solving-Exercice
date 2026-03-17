from datetime import date

Ano_nascimento = int(input("Digite o ano de nascimento do aluno: "))
ano_atual = date.today().year
idade = int( ano_atual - Ano_nascimento)


if idade <= 9:
    print("MIRIM")
elif 9 < idade <= 14:
    print("INFANTIL")
elif 14 < idade <= 19:
    print("JUNIOR")
elif 19 < idade <= 25:
    print("Senior")
else:
    print("MASTER")
