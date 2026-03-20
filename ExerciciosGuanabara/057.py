
while True:
    sexo = str(input("Digite o sexo: "))
    if sexo.upper() == "F" or sexo.upper() == "M":
        print(f"Sexo {sexo.upper()} registrado com sucesso")
        break

