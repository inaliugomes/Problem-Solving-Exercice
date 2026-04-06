alunos = []

continuar = True

while continuar:
    aluno_info = []
    nome = input("Qual o nome do aluno? ")
    nota1 = float(input("Qual a primeira nota do aluno? "))
    nota2 = float(input("Qual a segunda nota do aluno? "))
    aluno_info.append(nome)
    aluno_info.append(nota1)
    aluno_info.append(nota2)
    alunos.append(aluno_info)
    continuar = input("Deseja continuar? [S/N] ").upper()
    if continuar == "N":
        continuar = False

print("-="*20)

print(f"No.  NOME   MÉDIA")
print("-"*20)
for aluno in alunos:
    for c in range(0, 3):
        print(f" {aluno[c]:^5} ", end="")
    print()
print("-"*20)

parar = 0

while parar != 999:
    notas_aluno = int(input("Mostrar notas de qual aluno?(999 interrompe):"))
    if notas_aluno == 999:
        parar = notas_aluno
    else:
        print(f"Notas de {alunos[notas_aluno][0]} sao [{alunos[notas_aluno][1]}, {alunos[notas_aluno][2]}]")
