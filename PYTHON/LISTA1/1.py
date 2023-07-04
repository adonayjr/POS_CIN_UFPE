# Ler 3 números de tipo float, calcular a sua média aritmética, e imprimir os números juntamente com o resultado.
# E se os números forem inteiros?

# Leitura dos três números float
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Cálculo da média aritmética
media = (num1 + num2 + num3) / 3

# Impressão dos números e do resultado
print("Números digitados:", num1, num2, num3)
print("Média aritmética:", media)
