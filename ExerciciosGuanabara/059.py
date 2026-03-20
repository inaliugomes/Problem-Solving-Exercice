primero_numero = int(input("Primeiro valor: "))
segundo_numero = int(input("Segundo valor: "))

finalizar = False

while not finalizar:
    print("[ 1 ] somar")
    print("[ 2 ] multiplicar")
    print("[ 3 ] maior")
    print("[ 4 ] novos numeros")
    print("[ 5 ] sair do programa")
    opcao = int(input("Qual sua opcao: "))

    if opcao == 1:
        soma = primero_numero + segundo_numero
        print(f"A soma entre {primero_numero} + {segundo_numero} = {soma}")
    elif opcao == 2:
        multiplicar = primero_numero * segundo_numero
        print(f"A multiplicacao entre {primero_numero} * {segundo_numero} = {multiplicar}")
    elif opcao == 3:
        if segundo_numero > primero_numero:
            print(f"o {segundo_numero} é maior que o {primero_numero}")
        else:
            print(f"o {primero_numero} é maior que o {segundo_numero}")
    elif opcao == 4:
        primero_numero = int(input("Primeiro valor: "))
        segundo_numero = int(input("Segundo valor: "))
    elif opcao == 5:
        finalizar = True
    else:
        print("Valor invalido , tente novamente")