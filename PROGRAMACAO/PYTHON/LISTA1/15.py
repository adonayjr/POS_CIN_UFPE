# soluções usando os comandos for e while, respectivamente.
# Ler um número inteiro positivo e dizer se ele é primo ou não.

import math

num = int(input('num: '))
while num <2:
    num = int(input('invalido'))
raiz = int(math.sqrt(num))
di = 2

while (di <= raiz) and (num % di != 0):
    di = di + 1

if di > raiz:
    print(num, 'e primo')

else:
    print(num, 'nao e primo')