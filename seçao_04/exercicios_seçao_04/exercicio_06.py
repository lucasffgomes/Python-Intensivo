"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula de conversão é: F = C * (9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.
"""

print("Olá! Vamos descobrir a temperatura em Fahrenheit?")

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = celsius * (9.0/5.0) + 32.0

print("A temperatura em Fahrenheit é:", fahrenheit, "ºF")

print(type(celsius))
print(type(fahrenheit))




