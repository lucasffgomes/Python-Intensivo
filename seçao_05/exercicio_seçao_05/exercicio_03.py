"""
Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário,
imprima o número ao quadrado.
"""

print()
print("Vamos ler um número REAL.")

numero = int(input("Digite um número: "))

if numero > 0:
    print(int(numero ** (1/2)))
else:
    print(numero ** 2)


