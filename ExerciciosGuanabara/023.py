numero = input("Informe o seu numero")

separado = list(numero)
print(len(separado))

if len(separado)==1:
    print(f"Unidade: {separado[0]}")
    print(f"Dezena: 0")
    print(f"Centena: 0")
    print(f"Milhares: 0")
elif len(separado)==2:
    print(f"Unidade: {separado[1]}")
    print(f"Dezena: {separado[0]}")
    print(f"Centena: 0")
    print(f"Milhares: 0")
elif len(separado)==3:
    print(f"Unidade: {separado[2]}")
    print(f"Dezena: {separado[1]}")
    print(f"Centena: {separado[0]}")
    print(f"Milhares: 0")
else:
    print(f"Unidade: {separado[3]}")
    print(f"Dezena: {separado[2]}")
    print(f"Centena: {separado[1]}")
    print(f"Milhares: {separado[0]}")
