lista_numeros = []

for c in range(0,5):
    valor = int(input("Digite um valor: "))
    lista_numeros.append(valor)
    lista_numeros.sort()
    if lista_numeros.index(valor) == len(lista_numeros) - 1:
        print("Adicionado ao final da lista ...")
    else:
        print(f"Adicionado na posicao {lista_numeros.index(valor)} da lista...")

print(lista_numeros)