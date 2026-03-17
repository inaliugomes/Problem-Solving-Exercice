

print("-="*20)
print("Analisador de triangulo")
print("-="*20)
reta_1  = float(input("Qual o valor da reta 1: "))
reta_2 = float(input("Qual o valor da reta 2: "))
reta_3 = float(input("Qual o valor da reta 3: "))
if reta_1 + reta_2 > reta_3 and reta_1 + reta_3 > reta_2 and reta_2 + reta_3 > reta_1:
    print("Os tres segmentos podem formar um triangulo")
else:
    print("Os tres segmentos nao podem forma um triangulo")