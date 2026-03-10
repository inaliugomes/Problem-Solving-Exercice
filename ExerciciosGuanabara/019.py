from random import choice
primeiro = input("Digite o primeiro Nome: ")
segundo = input("Digite o segundo Nome: ")
tercero = input("Digite o tercero Nome: ")
quarto = input("Digite o quarto Nome: ")

alunos =  [primeiro, segundo, tercero, quarto]

sorteado = choice(alunos)

print(f"O aluno escolhido foi {sorteado}")