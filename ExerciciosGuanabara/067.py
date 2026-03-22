
while True:
    numero = int(input("Que tabuada quere ver"))
    print("-=" * 10)

    if numero >= 0:
        for c in range(1, 11):
            print(f"{numero} x {c} = {numero * c}")
    else:
        print("-=" * 10)
        print("PROGRAMA TABUADA ENCERRADO")
        print("-=" * 10)
        break

