"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
- O número digitado ao quadrado;
- A raiz quadrada do número digitado.
"""

print()
print("Vamos ler um número.")

numero = int(input("Digite um número: "))

if numero > 0:
    expoente = numero ** 2
    raiz = int(numero ** (1/2))
    print(f"O quadrado do número digitado será {expoente} e sua raiz quadrada será {raiz}.")
else:
    print("Número inválido.")






