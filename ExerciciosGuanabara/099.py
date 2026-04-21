from random import randint
from time import sleep

def linha():
    print('-='*20)

def encontrar_maior_numero(*nums):
    linha()
    for numero in nums:
        print(numero, end=' ')
        sleep(1)
    print(f"Foram informados {len(nums)} ao todo")
    print(f"O maior valor informado foi {max(nums)}")

encontrar_maior_numero(2,9,4,5,7,1)
encontrar_maior_numero(4,7,0)
encontrar_maior_numero(1,2)
encontrar_maior_numero(6)
encontrar_maior_numero(0)
