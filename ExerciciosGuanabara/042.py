segmento_1 = float(input("Digite o primeiro nota: "))
segmento_2 = float(input("Digite o segundo nota: "))
segmento_3 = float(input("Digite o terceiro nota: "))

if segmento_1 + segmento_2 > segmento_3 and segmento_1 + segmento_3 > segmento_2 and segmento_2 + segmento_3 > segmento_1:

    if segmento_1 == segmento_2 == segmento_3:
        print("É um triangulo Equilatero")
    elif segmento_1 != segmento_2 and segmento_2 != segmento_3 and segmento_3 != segmento_1:
        print("É um triangulo Escaleno")
    elif segmento_1 == segmento_2 or segmento_2 == segmento_3 or segmento_3 == segmento_1:
        print("É um triangulo Isosceles")
else:
    print("Os tres segmentos nao podem formar um triangulo")