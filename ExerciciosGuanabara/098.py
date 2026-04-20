def linha(incio=1,fim=11,contador=1):
    contadorStr = str(contador)
    print(f"Contagem de {incio} até {fim} de {contadorStr[1:]} em {contadorStr[1:]}")
    for c in range(incio,fim,contador):
        print(c,end=' ')
    print('FIM')
    print('-=' * 30)

print('-='*30)
linha()
linha(10,-2,-2)
Inicio = int(input("Inicio: "))
Fim = int(input("Fim: "))
Passo = int(input("Passo: "))

linha(Inicio,Fim,Passo)