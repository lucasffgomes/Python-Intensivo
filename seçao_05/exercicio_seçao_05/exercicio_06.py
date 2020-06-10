"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos.
"""

print()
print("Vamos descobrir a diferença entre dois números inteiros.")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    diferenca = numero1 - numero2
    print(f"O maior número será {numero1}, e a diferença entre eles será de {diferenca}.")
elif numero2 > numero1:
    diferenca = numero2 - numero1
    print(f"O maior número será {numero2}, e a diferença entre eles será de {diferenca}.")
else:
    print("Números iguais.")
