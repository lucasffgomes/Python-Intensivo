"""
Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. A
fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em
metros cúbicos.
"""

print()
print("Vamos converter o volume de METROS CÚBICOS para LITROS!")

metro_cubico = float(input("Digite o valor em Metro Cúbico: "))

litro = 1000 * metro_cubico

print()
print(f"O valor convetido para LITROS é de {litro}l. ")

