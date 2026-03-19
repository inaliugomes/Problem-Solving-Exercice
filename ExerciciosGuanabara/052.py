numero = int(input("Digite um numero: "))

numero_devisivel = 0
for c in range(1 , numero+1):
    if numero % c == 0:
        numero_devisivel += 1

if numero_devisivel <= 2:
    print("Esse  numero é primo")
else:
    print(f"o numero {numero} foi divisivel por pelo menos {numero_devisivel} valor")
