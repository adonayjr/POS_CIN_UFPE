# soluções usando os comandos for e while, respectivamente.
# Calcular o fatorial de um número inteiro lido.
numero = int(input("Digite um número inteiro: "))

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print("O fatorial de", numero, "é:", fatorial)


###################################################################################
numero = int(input("Digite um número inteiro: "))

fatorial = 1
i = 1

while i <= numero:
    fatorial *= i
    i += 1

print("O fatorial de", numero, "é:", fatorial)