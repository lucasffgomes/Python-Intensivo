"""
Leia um número inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""

print()
print("Vamos calcular o tempo com um número inteiro.")

segundos = int(input("Digite um número inteiro: "))

minuto = segundos // 60
resto_segundos = segundos % 60
segundos_final = resto_segundos

resto_minuto = minuto % 60
minuto_final = resto_minuto

print(minuto_final)
print(segundos_final)



"""
horas = numero_inteiro // 3600
minutos = numero_inteiro // 60
segundos = numero_inteiro

print(f"{horas} horas.")
print(f"{minutos} minutos.")
print(f"{segundos} segundos.")
"""

