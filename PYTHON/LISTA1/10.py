# Ler um número inteiro positivo N digitado pelo usario e depois ler N numeros inteiros positivos(0 < x < 4000) e, 
# para cada um deles. imprimir a sua representacao em algarismos romanos. 
# OBS: lembre qye os valores dos algarismos romanos são:
# I=1, V=5, X=10, L=50, C=100, D=500, e M=1000, e que IV=4, IX=9, XL=40, XC=90, CD=400 e CM=900.

lista = [(1000, 'M'), (900, 'CM'), (500,'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50,'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5,'V'), (4, 'IV'),(1,'I')]

n = int(input('n:'))
while n<1:
        n=int(input('invalido'))

for i in range(n):
            num = int(input('num: '))
            while (num<1) or (num>3999):
                num = int(input('invalido'))
            romano = ''
            aux = num

            for elem in lista:
                    while elem[0] <= aux:
                        romano = romano + elem[1]
                        aux = aux - elem[0]
            print(num, 'é', romano, 'em romanos')