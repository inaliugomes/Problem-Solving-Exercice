nome = str(input('Digite seu nome: '))

nome_sem_espaco = nome.replace(' ','').upper()
polindromo = nome_sem_espaco[::-1]


if polindromo == nome_sem_espaco:
    print(f"O inverso de {nome_sem_espaco} é {polindromo} entao é Palindromo")
else:
    print(f"O inverso de {nome_sem_espaco} é  {polindromo} entao nao é Palindromo")