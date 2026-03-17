valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salario? "))
anos = int(input("Quantos anos de financiamento? "))

prestacao = salario * 0.30
pagamento = (valor_casa / anos) / 12


if pagamento > prestacao:
    print(f"Voce pode pagar {prestacao:.2f} e o pagamentos idealmente {pagamento:.2f}, NEGADO")
else:
    print(f"Voce podem pagar {prestacao} e o pagamentos idealmente {pagamento:.2f} ACEITADO")