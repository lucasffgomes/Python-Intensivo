"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python

for item in iteravel:
    //execução do loop


Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- Strings
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)

# Exemplo de for 1 (Iterando em uma String)
for letra in nome:
    print(letra)
-----------------------------------------------------------------------------
# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)
-----------------------------------------------------------------------------------
# Exemplo de for 3 (Iterando sobre um Range)

range(valor_inicial, valor_final)
OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - NÃO!

for numero in range(1, 10):
    print(numero)

Enumerate:

(0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U'), (6, 'n'), (7, 'i'), (8, 'v'), (9, 'r')...

for indice, letra in enumerate(nome):
    print(nome[indice])

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)

nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)

--------------------------------------------------------------------------------------------

qtde = int(input("Quantas vezes esse loop deve rodar? "))
soma = 0

for n in range(1, qtde+1):
    numero = int(input(f"Informe o {n}/{qtde} valor: "))
    soma = soma + numero
print(f"A soma é {soma}")

------------------------------------------------------------------------------
nome = "Geek University"
for letra in nome:
    print(letra, end='') # Imprimir tudo na mesma linha
"""

# Original: U+1F60D
# Modificado: U0001F60D

emoji = 'U0001F60D'

for _ in range(2):
    for numero in range(1, 11):
        print(f"\U0001F60D" * numero)








