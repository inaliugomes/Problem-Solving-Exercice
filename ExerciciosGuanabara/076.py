print("-"*60)
print(f"{" "*20}LISTAGEM DE PRECOS")
print("-"*60)
material = (("Lápis","1.75"),("Borracha","2.00"),("Caderno","15.90"),("Estejo","25.00"),("Transferidor","4.20"),("Compasso","9.99"),
            ("Mochile","120.32"),("Canetas","22.30"),("Livro","34.90")
            )


for item in material:
    print(f"{item[0]}{"."*(30-len(item[0]))}R${" "*(7 - len(item[1]))}{item[1]}")

print("-"*60)