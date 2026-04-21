from datetime import datetime

def votar(ano):
    idade = datetime.now().year - ano

    if idade < 16:
        print(f"Tem {idade} nao pode votar")
    elif 16 <= idade < 50:
        print(f"Tem {idade} Obrigadorio votar")
    else:
        print(f"Tem {idade} Opcional votar")

ano_nascimento = int(input("Em que ano voces nasceu? "))
votar(ano_nascimento)


