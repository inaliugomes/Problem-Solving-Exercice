expresao = str(input("Digite a expressao: "))

lista_exp = []
conter_esc = 0
conter_drc = 0
for simbolo in expresao:
    lista_exp.append(simbolo)
    if simbolo == "(":
        conter_esc += 1

    if simbolo == ")":
        conter_drc += 1

if conter_esc == conter_drc:
    print("A sua expresao esta valida")
else:
    print("A sua expresao nao esta invalida")
