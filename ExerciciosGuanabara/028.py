from random import randint

numero = int(input("Informe um numero "))

numero_computador = randint(1,10)

if numero == numero_computador:
    print("Parabens! pensou no mesmo numero que eu ")
else:
    print("Perdeu , pensamos em numero diferente")