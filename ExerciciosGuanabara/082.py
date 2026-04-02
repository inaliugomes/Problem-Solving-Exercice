finalizar = False
lista_numeros = []
lista_par = []
lista_impar = []


while not finalizar:

    numero = int(input("Digite O seu numero: "))
    lista_numeros.append(numero)
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
    continuar =str(input("Deseja continuar? [S/N]")).upper()
    if continuar == "N":
        finalizar = True


print(f"A lista completo é {lista_numeros}")
print(f"A lista de pares é {lista_par}")
print(f"A lista de impares é {lista_impar}")