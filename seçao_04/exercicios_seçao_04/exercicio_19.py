"""
Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³. A
fórmula de conversão é: M = L / 1000, sendo L o volume em litros e M o volume em metros
cúbicos.
"""

print()
print("Vamos converter de LITROS para METROS CÚBICOS.")


litros = float(input("Digite o valor em LITROS: "))

metro_cubico = litros / 1000

print()
print(f"O valor convertido para METRO CÚBICO é de {metro_cubico}m³.")


