finalizar = False

lista_numeros = []

while not finalizar:
    numero = int(input("Digite um valor: "))
    if numero not in lista_numeros:
        lista_numeros.append(numero)
        print("Valor adicionado com sucesso...")
    else:
        print(f"O {numero} ja existe na lista")
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar in "Nn":
        finalizar = True

lista_numeros.sort()

print(lista_numeros)