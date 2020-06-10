"""
Sejam A e B os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = raiz(A² + B²). Faça um programa que receba os valores de A e B e calcule
o valor da hipotenusa através da equação. Imprima o resultado dessa operação.
"""

print()
print("Vamos descobrir o valor da HIPOTENUSA.")

catetoA = float(input("Digite o valor do cateto A: "))
catetoB = float(input("Digite o valor do cateto B: "))

hipotenusa = ((catetoA ** 2) + (catetoB ** 2)) ** 0.5

print(f"O valor da HIPOTENUSA será de: {hipotenusa}")



