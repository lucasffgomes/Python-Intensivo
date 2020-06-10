"""
Uma empresa vende o mesmo produto para quatro difentes estados. Cada estado
possui uma taxa diferente de imposto sobre o produto (MG 7%, SP 12%, RJ 15%,
MS 8%). Faça um programa em que o usuário entre com o valor e o estado
destino do produto e o programa retorne o preço final do produto acrescido do imposto do estado
em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem
de erro.
"""

print()
print("Opções de estado:")
print(" 1 = MG 7%")
print(" 2 = SP 12%")
print(" 3 = RJ 15%")
print(" 4 = MS 8%")
print()

preco_do_produto = float(input("Digite o preço do produto: "))
estado = int(input("Digite a opção de estado: "))

if estado == 1:
    preco_do_produto = preco_do_produto * (107/100)
    preco_do_produto = str(preco_do_produto).replace(".", ",")
    print(f"O preço com imposto será de R${preco_do_produto}")

elif estado == 2:
    estado = "São Paulo"
    preco_do_produto = preco_do_produto * (112/100)
    preco_do_produto = str(preco_do_produto).replace(".", ",")
    print(f"O preço com imposto para {estado} será de R${preco_do_produto}")

elif estado == 3:
    estado = "Rio de Janeiro"
    preco_do_produto = preco_do_produto * (115/100)
    preco_do_produto = str(preco_do_produto).replace(".", ",")
    print(f"O preço com imposto para {estado} será de R${preco_do_produto}")

elif estado == 4:
    estado = "Mato Grosso do Sul"
    preco_do_produto = preco_do_produto * (108/100)
    preco_do_produto = str(preco_do_produto).replace(".", ",")
    print(f"O preço com imposto para {estado} será de R${preco_do_produto}")
else:
    print("Valor de Estado Inválido.")
