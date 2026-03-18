from random import randint
print(f"{"="*10} JO KEN PO {"="*10}")
print("Sua opcoes")
print("[ 0 ] PEDRA")
print("[ 1 ] PAPEL")
print("[ 2 ] TESOURA")

opcao = int(input("Sua opcao: "))

opcao_computador = randint(0,2)

print(opcao_computador)