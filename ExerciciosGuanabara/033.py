primeiro_Valor = int(input("Primeiro Valor: "))
segundo_Valor = int(input("Segundo Valor: "))
terceiro_Valor = int(input("Terceiro Valor: "))

if primeiro_Valor > segundo_Valor and primeiro_Valor > terceiro_Valor:
    print(f"O maior valor {primeiro_Valor}")
    if segundo_Valor > terceiro_Valor:
        print(f"O menor valor {terceiro_Valor}")
    else:
        print(f"O menor valor {segundo_Valor}")
elif segundo_Valor > primeiro_Valor and segundo_Valor > terceiro_Valor:
    print(f"O maior valor {segundo_Valor}")
    if primeiro_Valor > terceiro_Valor:
        print(f"O menor valor {terceiro_Valor}")
    else:
        print(f"O menor valor {primeiro_Valor}")
else:
    print(f"O maior valor {terceiro_Valor}")
    if primeiro_Valor > segundo_Valor:
        print(f"O menor valor {segundo_Valor}")
    else:
        print(f"O menor valor {primeiro_Valor}")