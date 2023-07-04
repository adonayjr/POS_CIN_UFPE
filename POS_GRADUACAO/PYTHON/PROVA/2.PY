'''
Q2- Faça um programa Python para ler uma sequencia de números inteiros a leitura para
quando o número -999999 for lido. No entanto, o usuário só deve poder digitar
no máximo 250 números. O programa deve iomprimir as seguintes informações como resultado:

* A quantidade total de números lidos.
* Os números lidos cujos valores tiverem 3 dígitos significativos. A impressão destes númeors deve mostrar primeiro
os números negativos ( de 3 dígitos), na mesma ordem relativa em que foram
lidos, e depois positivos(idem).
'''

numeros = []
numeros_neg = []
numeros_pos = []
limitador = 10
soma_pos = 0
menor = -1

n = int(input("Digite uma sequência de números inteiros (-999999 para parar): "))
while n != -999999 and len(numeros) < limitador:
    if(-999 < n < -100):
        numeros_neg.append(n)
    if(100 < n < 999):
        numeros_pos.append(n)
    if(menor < 0) and n > 0:
        menor = n
    numeros.append(n)
    if(len(numeros) < limitador):
        n = int(input("Digite uma sequência de números inteiros (-999999 para parar): "))
    else:
        print("Número máximo de termos atingido")

print("Quantidade total de números: " + str(len(numeros)))

print("Números negativos de 3 dígitos:")
print(numeros_neg)

print("Números positivos de 3 dígitos:")
print(numeros_pos)

for i in range(len(numeros_pos)):
    soma_pos = soma_pos + numeros_pos[i]
print("Soma dos números positivos de 3 dígitos: ", str(soma_pos))

for i in range(len(numeros_pos)):
    if(menor > numeros_pos[i]):
        menor = numeros_pos[i]
print(menor)  