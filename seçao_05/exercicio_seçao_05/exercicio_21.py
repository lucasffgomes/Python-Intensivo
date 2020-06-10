"""
Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhi-
da. Escreva uma mensagem de erro se a opção foi inválida.

Escolha a opção:
1- Soma de 2 números.
2- Diferença entre 2 números (maior pelo menor).
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero).
"""
# Na divisão o primeiro tem que ser maior que o segundo.

print()
print("Vamos programar.")

numero = int(input("Escolha um número de 1 à 4: "))

if numero == 1:
    print("Soma de 2 números.")
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    resultado = valor1 + valor2
    print(f"A soma será de {resultado}.")

elif numero == 2:
    print("Diferença entre 2 números.")
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    if valor1 > valor2:
        resultado = valor1 - valor2
        print(f"A diferença será de {resultado}.")
    elif valor2 > valor1:
        resultado = valor2 - valor1
        print(f"A diferença será de {resultado}.")

elif numero == 3:
    print("Produto entre 2 números.")
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    resultado = valor1 * valor2
    print(f"A multiplicação será de {resultado}.")

elif numero == 4:
    print("Divisão de 2 números.")
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    if valor1 > valor2:
        resultado = valor1 / valor2
        print(f"A divisão será de {resultado}.")
    elif valor2 > valor1:
        resultado = valor2 / valor1
        print(f"A divisão será de {resultado}.")
    elif valor1 == valor2:
        print("O resultado sempre será 1.")

else:
    print("Escolha um número válido.")