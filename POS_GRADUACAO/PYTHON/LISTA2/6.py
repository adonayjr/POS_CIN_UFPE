# Ler uma lista de N números (N é informado pelo usuário antes), 
# e depois criar duas outras listas com os números pares e ímpares separados. No final imprimir as 3 listas. 



numeros = []
pares = []
impares = []

n = int(input("Digite a quantidade de números: "))

for i in range(n):
    numero = float(input("Digite o número: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print('numeros: ', numeros)
print('pares: ', pares)
print('impares: ', impares)


               