"""
Estruturas Lógicas
    and (E)
    or (OU)
    not (NÃO)
    is (É)

Operadores unários:
    - not, is
Operadores binários:
    - and, or

Para o AND ambos os valores precisam ser True;
Para o OR um ou outro valor precisa ser True;
Para o NOT o valor do booleano é invertido; True>False False>True

"""

ativo = True
logado = False

if ativo or logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta, cheque seu E-mail.')

print('----------------------------------------------')

if not ativo:
    print("Você precisa ativar sua conta, cheque seu E-mail.")
else:
    print("Bem-vindo usuário.")


# ativo é True?
print(ativo is True)








