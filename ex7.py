total = 0

while True:
    preco = float(input("Digite o preço do produto: "))
    print("<Digite 0 caso queria encerrar a operação>")
    if preco == 0:
        break
    else:
        quantidade = int(input("Digite a quantidade: "))
        total += (preco*quantidade)
if total == 0:
    print("Não houve produtos informados.")
else:
    print("Total= R$", total)
