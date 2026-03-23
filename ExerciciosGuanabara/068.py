from random import randint


computer = randint(0, 10)

my_result = int(input('Digite um valor: '))

par_impar = str(input("Digite [P/I]"))

resultado = my_result + computer
print(resultado)
if resultado % 2 == 0 :
    if par_impar.upper() == 'P':
        print("Voce ganhou")
    else:
        print("Voce perdeu")
else:
    if par_impar.upper() == 'I':
        print("Voce ganhou")
    else:
        print("Voce perdeu")

