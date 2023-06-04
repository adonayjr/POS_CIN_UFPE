# soluções usando os comandos for e while, respectivamente.
# Somar os inteiros pares entre 50 e 100 (inclusive).

soma = 0

for num in range(50, 101):
    if num % 2 == 0:
        soma += num

print("A soma dos inteiros pares é:", soma)

###################################################################################
soma = 0
num = 50

while num <= 100:
    if num % 2 == 0:
        soma += num
    num += 1

print("A soma dos inteiros pares é:", soma)