"""
Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = C / 2.54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.
"""

print()
print("Vamos converter um comprimento de CENTÍMETROS para POLEGADAS.")

centimetro = float(input("Digite o valor do comprimento em centímetros: "))

polegada = centimetro / 2.54

print()
print(f"O valor em POLEGADAS é {polegada}.")
print('FIM.')