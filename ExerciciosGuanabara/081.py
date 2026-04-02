finalizar = False

valores = []

while not finalizar:
    valor = int(input("Digite um valor: "))
    valores.append(valor)
    continuar = str(input("Deseja continuar? [S/N] "))
    if continuar in "Nn":
        finalizar = True

valores.sort(reverse=True)
print(f"Voce digitou {len(valores)} elementos")
print(f"Os valores em ordem decrescente sao {valores}")
if 5 in valores:
    print("O valor 5 faz parte da lista")
