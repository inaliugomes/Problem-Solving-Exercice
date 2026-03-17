
base = int(input("Qual o seu base? "))

print("Escolha uma das bases para conversao")
print("[ 1 ] converter para BINARIO")
print("[ 2 ] converter para Octal")
print("[ 3 ] converter para Hexadecimal")

escolha = str(input("Qual a sua escolha? "))

hexa = hex(base)
binario = bin(base)
octal = oct(base)

if escolha != "1" and escolha != "2" and escolha != "3":
    print("Essa escolha nao faz parte das opcoes")
elif escolha == "1":
    print(f"{base} convertido para BINARIO {binario[2:]}")
elif escolha == "2":
    print(f"{base} convertido para OCTAL {octal}")
elif escolha == "3":
    print(f"{base} convertido para HEXADECIMAL {hexa[2:]}")

