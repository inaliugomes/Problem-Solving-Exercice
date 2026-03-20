primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))

contador = 1

while contador <= 10:
    print(f'{primeiro_termo}',end='-> ')
    primeiro_termo += razao
    contador += 1
    if contador == 10:
        break
print('FIM')