"""
Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
- o total a pagar com desconto de 10%;
- o valor de cada parcela, no parcelamento de 3X sem juros;
- a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
- a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""

print("Vamos ajudar os vendedores.")
print()

valor_total = float(input("Digite o valor R$ "))

descontado = valor_total - (valor_total * (10 / 100))
parcelado = valor_total / 3
comissao_a_vista = descontado * (5 / 100)
comissao_parcelada = valor_total * (5 / 100)


print(f"O valor com desconto de 10% será de R$ {descontado}")
print(f"O valor parcelado em 3X sem juros será de R$ {parcelado}")
print(f"A comissão do vendedor na venda a vista será de R$ {comissao_a_vista}")
print(f"A comissão do vendedor na venda parcelada será de R$ {comissao_parcelada}")




