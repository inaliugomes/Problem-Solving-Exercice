from datetime import datetime
nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = datetime.today().year
ano_de_nascimento = ano_atual - nascimento

if ano_de_nascimento < 18:
    resta = 18 - ano_de_nascimento
    alistamento = ano_atual + resta
    print(f"Quem nasceu em {nascimento} tem {ano_de_nascimento} anos  em {ano_atual}")
    print(f"Ainda falta {resta} para o alistamento")
    print(f"O seu alistamento sera em {alistamento}")
elif ano_de_nascimento == 18:
    print("Voce tem que se alistar IMEDIATAMENTE")
else:
    print("Voce ja deveria estar alistado")

