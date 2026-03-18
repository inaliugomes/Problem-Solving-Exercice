peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

IMC = peso / (altura * altura)
print(IMC)
if IMC < 18.5:
    print("Abaixo do peso")
elif 18.5 <= IMC <= 25:
    print("Peso ideal")
elif 25 <= IMC <= 30:
    print("Sobrepeso")
elif 30 <= IMC <= 40:
    print("Obesidade")
else:
    print("Obesidade morbida")