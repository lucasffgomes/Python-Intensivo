"""
Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro
em um percurso, calcule o consumo em KM/l e escreva uma mensagem de acordo com
a tabela.
           |   CONSUMO   | (Km/l) |     MENSAGEM     |
           |   menor que |   8    | Venda o carro!   |
           |     entre   | 8 e 14 | Econômico!       |
           |   maior que |   12   | Super econômico! |
"""

print()
print("Vamos descobrir se o carro ta valendo a pena.")

distancia = int(input("Digite a distância em Quilômetros: "))
litros_de_gasolina = float(input("Digite quantos litros foram usados: "))

consumo = distancia / litros_de_gasolina

print(f"O consumo foi de {consumo}km/l")

if consumo < 8:
    print("Venda o carro!")
elif 8 >= consumo or consumo < 14:
    print("Econômico!")
elif consumo > 12:
    print("Super econômico.")


