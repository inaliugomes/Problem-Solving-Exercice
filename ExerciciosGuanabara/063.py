paragem = 0
numero_digitado = 0
soma = 0
while paragem != 999:
    numero = int(input("Informe um numero [999 para parar]: "))
    if numero != 999:
        soma += numero
        numero_digitado += 1
    else:
        paragem = numero

print(f"Voce digitou {numero_digitado} numeros e a soma entre eles foi {soma}")
