# Ler por linhas uma matriz M x N, onde M <= 4 e N <= 8 são lidos antes da leitura da matriz. 
# Depois, percorrendo a matriz por colunas, armazenar em uma lista os elementos desta matriz que sejam múltiplos de 
# 6. No final, imprimir de maneira organizada a matriz e o vetor.



m = int(input('num linhas: '))
while m < 1 or m > 4:
    m = int(input('num linhas: '))

n = int(input('num. colunas: '))
while n < 1 or n > 8:
    n = int(input('num. colunas: '))

lista = [0] * (m*n)
mult6 = 0

mat = []
for i in range (m):
    mat.append([0] * n)

for i in range (m):
    for j in range (n):
        mat[i][j] = int(input('elemento'+ str(i) + '.' + str(j) + ': '))
print(mat)

for j in range (n):
    for i in range (m):
        if mat[i][j] % 6 == 0:
            lista[mult6] = mat[i][j]
            mult6 = mult6 + 1
print(lista)
lista = lista[:mult6]

for i in range (m):
    print(mat[i])
print(lista)