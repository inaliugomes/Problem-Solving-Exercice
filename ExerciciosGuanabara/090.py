aluno = {"Nome": str(input("Nome: ")), "media": float(input("Media: "))}

if aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Aprovado'

for k, v in aluno.items():
    print(f"- {k} é igual  {v}")