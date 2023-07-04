# soluções usando os comandos for e while, respectivamente.
# Somar os inteiros ímpares entre dois valores inteiros informados pelo usuário
inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))

soma = 0

for num in range(inicio, fim + 1):
    if num % 2 != 0:
        soma += num

print("A soma dos inteiros ímpares é:", soma)

###################################################################################
inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))

soma = 0
num = inicio

while num <= fim:
    if num % 2 != 0:
        soma += num
    num += 1

print("A soma dos inteiros ímpares é:", soma)