cidade = input("Informe a cidade onde nasceu")

separado = cidade.split(" ")


if separado[0].lower() == "santo":
    print(True)
else:
    print(False)