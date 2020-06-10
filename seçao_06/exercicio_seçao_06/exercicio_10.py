"""
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
"""

soma = 0

for i in range(0, 50):
    if i % 2 == 0:
        print(i)
        soma += i

print(f"A soma final é {soma}")

