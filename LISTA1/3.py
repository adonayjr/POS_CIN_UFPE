# Leitura dos números
numeros = []

n = int(input("Digite a quantidade de números: "))

for i in range(n):
    numero = float(input("Digite o número: "))
    numeros.append(numero)

# Verificação do menor número
menor_numero = min(numeros)

# Impressão do menor número
print("O menor número é:", menor_numero)