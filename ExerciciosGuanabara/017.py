from math import sqrt
cateto_oposto = float(input("Digite o cateto oposto: "))
cateto_adjacente = float(input("Digite o cateto adjacente: "))

c = sqrt(cateto_oposto*cateto_oposto + cateto_adjacente*cateto_adjacente)

print(f"A hipotenusa vai medir {c:.2f}")