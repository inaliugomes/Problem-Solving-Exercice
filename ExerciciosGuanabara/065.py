media = 0
maior = 0
menor = 0
total_digitado = 0
parar = False

while not parar:
    numero = int(input("Digite um numero"))
    total_digitado += 1
    media += numero
    if total_digitado == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    paragem = str(input("Deseja continuar? [S/N]"))

    if paragem.upper() == "N":
        parar = True

media_final = media / total_digitado

print(f"Voce digitou {total_digitado} e a media foi {media_final}")
print(f"O maior numero foi {maior} e o menor foi {menor}")
