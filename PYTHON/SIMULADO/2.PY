# Q2 — Faça um programa Python para ler uma sequencia de números inteiros negativos — 
# a leitura pára quando o número zero for lido, No entanto, o usuário só deve poder digitar no máximo 
# 150 números negativos, O programa deve imprimir as seguintes informações como resultado (nesta ordem): 
# * Os números lidos cujos valores têm 2 dígitos significativos e também são múltiplos de 5. 
#   A impressão destes números deve ser feita na ordem inversa da que foram lidos. 
# * O maior número lido que não seja múltiplo de 7.  ------------------ Valor da questão: 3,0 

num = int(input('Digite uma lista de números negativos(0 => parar): '))
negativos = []
mult = []
maior = []
cont = 0


while num < 0 and cont < 5: 
    cont = cont + 1
    negativos.append(num)
    num = int(input('Digite uma lista de números negativos(0 => parar): '))
    if num >= 0:
            print('Código parou')
for num in negativos:
    if num%5 == 0:
        mult.append(num)   
        mult.reverse()
        print('lista multiplos de 5 inverso: ', mult)
for num in negativos:
    if num %7 != 0 :
        maior.append(num)  
        print('maior não multiplo de 7: ',maior)
print(negativos)