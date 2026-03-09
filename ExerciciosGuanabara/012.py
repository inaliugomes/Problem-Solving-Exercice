produto = float(input("Informe o valor do produto: "))

descontoValor = produto * 0.05
valor_sem_desconto = produto - descontoValor

print(f"O produto que custva {produto}, na promoçao com desconto de 5% va custar {valor_sem_desconto:.2f}")