qtd = 0
qtd5 = 0
mult5 = [0]*150
maiorNaoMult7 = -999999999999

num = int(input("Digite um número negativo: "))
while num >= 0 :
    num = int(input("Digite pelo menos um número negativo: "))
    
while num != 0 and qtd < 150 :
    qtd += 1
    if (num % 5 == 0) and (num > -100) and (num < -9) :
        mult5[qtd5] = num
        qtd5 = qtd5 + 1
    if (num % 7 != 0) and (num > maiorNaoMult7) :
        maiorNaoMult7 = num

    num = int(input("digite outro número negativo, 0 p/parar: "))
    while num > 0 :
        num = int(input("Digite um número negativo, 0 p/parar: "))

if num < 0 :
    print("Quant. máxima de números atingida, último número foi descartado!")
    
if qtd5 == 0 :
    print("Nenhum múltiplo de 5 com 2 dígitos foi digitado.")
else:
    mult5 = mult5[0:qtd5]
    mult5.reverse()
    print("Múltiplos de 5 com 2 dígitos significativos:", mult5)

if  maiorNaoMult7 == -999999999999 :
    print("Nenhum não múltiplo de 7 foi digitado.")
else:
    print("O maior não múltiplo de 7 é", maiorNaoMult7)