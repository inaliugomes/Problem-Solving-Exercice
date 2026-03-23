print("*="*15)
print("Registar Pessoa")
print("*="*15)

pessoa_velha = 0
homens = 0
mulheres_menor = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()
    if sexo == 'M':
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres_menor += 1
    if idade >= 18:
        pessoa_velha += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print(f"Total de pessoas: {homens} homens")
print(f"Total de mulheres : {mulheres_menor} com menos de 20 anos")
print(f"total de pessoa com mais de 18 anos {pessoa_velha}")