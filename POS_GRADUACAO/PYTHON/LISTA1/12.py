# soluções usando os comandos for e while, respectivamente.
# Calcular a média aritmética de vários números reais fornecidos pelo usuário.
# A leitura dos números deve parar quando um número negativo for lido.

numeros = []
qtd = 1

numero = float(input("Digite o nota 1: "))

while numero >= 0:
        qtd+=1
        numeros.append(numero)
        numero = float(input(f"Digite o nota {qtd}: "))
        if numero < 0:
            print("Não é possivel inserir numero negativo") 
        
media = (sum(numeros))/len(numeros)
print("A media aritmetica é: ", media)
