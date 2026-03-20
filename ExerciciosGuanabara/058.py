from random import randint
computador_random = randint(0,10)
numero_tentativa = 1
print("Sou seu computador")

print("Vou pensar em um numero entre 0 e 10")
print("Será que consegue advinhar qual foi?")

palpite = int(input("Cual é seu palpite"))

while computador_random != palpite:
    if palpite < computador_random:
        print("O computador escolheu um numero maior , tente outra vez!")
        numero_tentativa += 1
    else:
        print("O computador escolheu um numero menor , tente outra vez!")
        numero_tentativa += 1
    palpite = int(input("Cual é seu novo palpite"))

print(f"Acertou com {numero_tentativa} tentativas")
