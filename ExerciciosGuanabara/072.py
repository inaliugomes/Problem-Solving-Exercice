numeros_por_extenso = [
    "zero", "um", "dois", "três", "quatro",
    "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "catorze",
    "quinze", "dezesseis", "dezessete", "dezoito",
    "dezenove", "vinte"
]
numero = int(input("Informe numero de 0 a 20: "))
while True:

    if numero <= 20:
        break
    else:
        numero = int(input("Informe numero de 0 a 20: "))

print(f"O numero {numero} por extenso é {numeros_por_extenso[numero]}")

