# soluções usando os comandos for e while, respectivamente.
# Calcular o menor de uma série de números inteiros lidos. 
# A leitura dos números deve parar quando o número zero for lido.

numeros = []

n = int(input("Digite a quantidade de números: "))

for i in range(n):
    numero = float(input("Digite o número: "))
    numeros.append(numero)

# Verificação do menor número
menor_numero = min(numeros)

# Impressão do menor número
print("O menor número é:", menor_numero)