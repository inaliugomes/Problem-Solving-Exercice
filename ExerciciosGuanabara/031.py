km = int(input("Informe a quantidade de KM:"))

resultado = 0
if km <= 200:
    resultado = km * 0.50
else:
    resultado = km * 0.45

print(resultado)