nome = input('Qual o seu nome?')

separado =nome.split()

print(separado)

for p in separado:
    if p.lower() == "silva":
        print(True)
