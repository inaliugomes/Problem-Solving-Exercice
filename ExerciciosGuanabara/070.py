print("=*"*10)
print("LOJA SUPER BARATA")
print("=*"*10)

continuar = 'S'
total = 0
produto_maior = 0
produto_menor = 0
produto_maior_nome = ""
produto_menor_nome = ""

while continuar == 'S':
    produto = str(input('Digite o nome do produto: '))
    preco = int(input("Informe o preco"))
    total += preco
    if preco > produto_maior:
        produto_maior = preco
        produto_maior_nome = produto
    if produto_menor == 0:
        produto_menor = preco
        produto_menor_nome= produto
    if preco < produto_menor:
        produto_menor = preco
        produto_menor_nome = produto
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print(f"----------------FIM DO PROGRAMA------------------")
print(f"O total da compra foi {total}")
print(f"Produto mas caro custa {produto_maior}")
print(f"Produto mais barato custa {produto_menor}")
