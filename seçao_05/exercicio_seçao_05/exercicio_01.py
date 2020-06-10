"""
Faça um programa que receba dois números e mostre qual deles é o maior.
"""

print()
print("Vamos descobrir qual número é maior.")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo valor: "))

if numero1 > numero2:
    print("O primeiro número é maior!")
elif numero2 > numero1:
    print("O segundo valor é maior!")
else:
    print("Os dois números são iguais!")