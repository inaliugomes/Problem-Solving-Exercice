numero = [int(input(f"Digite o {i+1}: ")) for i in range(7)]

pares = sorted([n for n in numero if n % 2 == 0])
impar = sorted([n for n in numero if n % 2 != 0 ])

print(f"Os valores pares digitados foram: {pares}")
print(f"Os valores impares digitados foram: {impar}")