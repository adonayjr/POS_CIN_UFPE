# soluções usando os comandos for e while, respectivamente.
# Calcular o menor de uma série de números inteiros lidos. 
# A leitura dos números deve parar quando o número zero for lido.


numero = int(input("Digite uma sequencia de numeros: 0->Parar: "))
numeros = []

while numero > 0:
    numeros.append(numero)
    numero = int(input("Digite uma sequencia de numeros: 0->Parar: "))
    if numero <= 0:
        print('Código parou')

# Verificação do menor número
menor_numero = min(numeros)

# Impressão do menor número
print("O menor número é:", menor_numero)