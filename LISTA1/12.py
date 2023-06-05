# soluções usando os comandos for e while, respectivamente.
# Calcular a média aritmética de vários números reais fornecidos pelo usuário.
# A leitura dos números deve parar quando um número negativo for lido.

numeros = []

n = int(input("Digite quantas notas para calcular: "))

for i in range(n):
    numero = float(input("Digite o número: "))
    if numero >= 0:
        numeros.append(numero)
    else:
        print("Não é possivel inserir numero negativo")
        break
media = (sum(numeros))/n
print("A media aritmetica é: ", media)
