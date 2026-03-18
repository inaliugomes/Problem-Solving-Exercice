from random import randint
print(f"{"="*10} JO KEN PO {"="*10}")
print("Sua opcoes")
print("[ 0 ] PEDRA")
print("[ 1 ] PAPEL")
print("[ 2 ] TESOURA")

opcao = int(input("Sua opcao: "))

opcao_computador = randint(0,2)


if opcao == 0:
    if opcao_computador == 0:
        print("Voce jogou Pedra o computador jogou pedra EMPATE!")
    elif opcao_computador == 1:
        print("Voce jogou Pedra o computador jogou Papel COMPUTADOR GANHOU!")
    else:
        print("Voce jogou Pedra o computador jogou TESOURA VOCE GANHOU!")
elif opcao == 1:
    if opcao_computador == 0:
        print("Voce jogou PAPEL o computador jogou PEDRA VOCE GANHOU!")
    elif opcao_computador == 1:
        print("Voce jogou PAPEL o computador jogou Papel  EMPATE!")
    else:
        print("Voce jogou PAPEL o computador jogou TESOURA COMPUTADOR GANHOU!")
elif opcao == 2:
    if opcao_computador == 0:
        print("Voce jogou TESOURA o computador jogou PEDRA COMPUTADOR GANHOU!")
    elif opcao_computador == 1:
        print("Voce jogou TESOURA o computador jogou Papel  VOCE GANHOU!")
    else:
        print("Voce jogou TESOURA o computador jogou TESOURA  EMPATE!")



