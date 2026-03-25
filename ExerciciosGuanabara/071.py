print("="*20)
print("BANCO CEV")
print("="*20)
nota = int(input("Qual a nota do produto? "))




nota_50 = nota//50
resto_50 = nota%50


nota_20 =resto_50//20
resto_20 = resto_50%20

nota_10 = resto_20//10
resto_10 = resto_20%10

print(nota_50)
print(nota_20)
print(nota_10)
