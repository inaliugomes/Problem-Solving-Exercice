salario = float(input("Informe o seu salario: "))

if salario > 1250:
    aumento = salario * 0.10
    final = salario + aumento
    print(f"Quem ganhava {salario} passa a ganhar  {final} ")
else:
    aumento = salario * 0.15
    final = salario + aumento
    print(f"Quem ganhava {salario} passa a ganhar  {final} ")