largura = float(input("Informe a largura da parede: "))
altura = float(input("Infor a altura da parede: "))

dimensao = largura * altura
tinta = dimensao / 2

print(f"Sua parede tem a dimensao de {largura}x{altura} e sua área é de {dimensao}")
print(f"Para pintar essa parede, voce precisará de  {tinta} litros de tinta")
