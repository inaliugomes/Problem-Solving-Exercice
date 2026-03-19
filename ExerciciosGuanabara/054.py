from datetime import datetime

ano_atual = datetime.now().year
maior_idade = 0
menor_idade = 0
for c in range(1,8):
    ano = int(input(f"Em que ano a {c} pessoa nasceu? "))
    if ano_atual - ano < 18:
        menor_idade += 1

    else:
        maior_idade += 1



print(f"Ao todo tivemos {maior_idade} maiores de idade")
print(f"E tambem tivemos {menor_idade} menores de idade")