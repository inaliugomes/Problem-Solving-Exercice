lista_valores = []
maior_valor = 0
menor_valor = 0

for i in range(0,5):
    valor = int(input("Digite um valor: "))
    lista_valores.append(valor)

lista_ordenado = sorted(lista_valores)

menor_valor = lista_ordenado[0]
maior_valor = lista_ordenado[-1]

print(f"Voce digitou os valores {lista_valores}")
print(f"O maior valor digitado foi {maior_valor} nas posicoes ", end="")
for v,p in enumerate(lista_valores):
    if p == maior_valor:
        print(f"{v}...",end=" ")
print(f"\nO menor valor digitado foi {menor_valor} nas posicoes ", end="")
for v,p in enumerate(lista_valores):
    if p == menor_valor:
        print(f"{v}...",end=" ")