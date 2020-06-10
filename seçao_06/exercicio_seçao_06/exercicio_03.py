"""
Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva
na tela, iniciando em 10 e terminando em 0. Mostrar uma mensagem "FIM!" após a
contagem.
"""
n = 11

while n > 0:
    n += -1
    print(n)
    if n == 0:
        print("Fim.")

