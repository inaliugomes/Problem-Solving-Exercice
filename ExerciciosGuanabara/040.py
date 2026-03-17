primeira_nota = float(input("Primeira nota: "))
segunda_nota = float(input("Segunda nota: "))

media = (primeira_nota + segunda_nota) / 2

if media >= 7:
    print(f"Tirando {primeira_nota} e {segunda_nota} a media do aluno {media:.1f}")
    print("APROVADO!")
elif media >5 and media <=7:
    print(f"Tirando {primeira_nota} e {segunda_nota} a media do aluno {media:.1f}")
    print("RECUPERACAO!")
else:
    print(f"Tirando {primeira_nota} e {segunda_nota} a media do aluno {media}")
    print("REPROVADO!")