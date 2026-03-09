dias = int(input("Informe a quantidade de dias alugados: "))
km = int(input("Informe a quantidade de km percorrido: "))

valor_por_dia = dias * 60

valor_por_km = km * 0.15

valor_total = valor_por_dia + valor_por_km

print(f"O total a pagar é de {valor_total:.2f} reais")