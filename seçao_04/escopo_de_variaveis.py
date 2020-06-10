"""
Escopo de Variáveis

Dois casos de escopo:

1 - Variáveis Globais;
    - Variáveis Globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis Locais;
    - Variáveis Locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao
    bloco onde foi declarada.


Para declarar variáveis em Python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinânima. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor à mesma.

"""

numero = 42  # Exemplo de VARIÁVEL GLOBAL
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

numero = 42

if numero > 10:
    novo = numero + 10  # Exemplo de VARIÁVEL LOCAL
    print(novo)

print(novo)












