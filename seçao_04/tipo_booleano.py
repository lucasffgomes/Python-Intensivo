"""
Tipo Booleano
Álgebra Booleana, craida por George Boole

2 constantes, VERDADEIRO ou FALSO  (True e False)
OBS: Sempre com a inicial maiúscula

Errado -> true, false
Certo -> True, False
"""

ativo = True
print(ativo)

"""
Operações Básicas
"""

# --------------------------- NEGAÇÃO (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso, se for falso o resultado será verdadeiro.
Ou seja, sempre o contrário.
"""
print(not ativo)

logado = False

# --------------------------- OU (or):
"""
É uma operação binária, ou seja, depende de dois valores. Um dos dois deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""

print(ativo or logado)

# -------------------------- E (and):
"""
Operação binária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiros

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""















