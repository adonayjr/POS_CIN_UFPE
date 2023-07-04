# Ler um número inteiro N e imprimir o valor do n-ésimo termo da sequência a seguir [-1,0,5,6, 11,12, 17,18, ...]
N = int(input("Digite o valor de N: "))

termo = 0
contador = 0

for i in range(N):
    if i % 2 == 0:
        termo -= 1
    else:
        termo += 5
    contador += 1

print("O valor do", N, "termo é:", termo)

###################################################################################
N = int(input("Digite o valor de N: "))

termo = 0
contador = 0

while contador < N:
    if contador % 2 == 0:
        termo -= 1
    else:
        termo += 5
    contador += 1

print("O valor do", N, "termo é:", termo)