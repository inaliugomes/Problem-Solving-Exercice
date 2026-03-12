nome = input("Digite seu nome: ")

nome_sem_espaco = nome.strip().upper()

primeiro_letra = nome_sem_espaco.find("A")

ultimo_letra = nome_sem_espaco.rfind("A")

if primeiro_letra == 0:
    print("1")
else:
    print(primeiro_letra)

print(ultimo_letra)
print(nome_sem_espaco.count("A"))
