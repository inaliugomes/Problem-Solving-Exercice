from xml.dom.minidom import ProcessingInstruction

print("-="*20)
print(f"{" "*12}LOJA DO PYTHON")
print("-="*20)

preco = float(input("Informe o valor da sua compra: "))

print("Forma de pagamento")
print("[ 1 ] a vista dinheiro/cheque")
print("[ 2 ] a vista cartao")
print("[ 3 ] 2x no cartao")
print("[ 4 ] 3x ou mais no cartao")

opcao = int(input("Qual a sua opcao: "))

if opcao == 1:
    desconto = preco - (preco * 0.10)
    print(f"Com a compra {preco} e pagamento a vista tem um desconto de 10 % pagará no total {desconto}")
elif opcao == 2:
    desconto = preco - (preco * 0.05)
    print(f"Com a compra {preco} e pagamento a vista tem um desconto de 5 % pagará no total {desconto}")
elif opcao == 3:
    print(f"O preco total a pagar {preco}")
elif opcao == 4:
    parcelamento = int(input("Quantas parcelas? "))
    juros = preco + (preco * 0.20)
    parcela = juros/parcelamento

    print(f"A sua compra será parcelada em {parcelamento} de R$ {parcela} com juros")
    print(f"A sua compra de {preco} vai custar {preco + parcela} no final ")
    print("-="*20)