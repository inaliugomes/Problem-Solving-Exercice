numero1 = int(input("Qual o primeiro valor? "))
numero2 = int(input("Qual o segundo valor? "))

if numero1 > numero2:
    print(f"{numero1} é maior que {numero2}")
elif numero1 < numero2:
    print(f"{numero2} é maior que {numero1}")
else:
    print(f"{numero1} e {numero2} sao iguais")