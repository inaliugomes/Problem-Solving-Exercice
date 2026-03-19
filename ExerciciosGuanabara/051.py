primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))


for c in range(1,11):
    print(f'{primeiro_termo}',end='-> ')
    primeiro_termo += razao

print("ACABOU")