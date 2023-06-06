# Fazer subrotinas recursivas para calcular o valor das seguintes séries — com n termos, 
# onde n deve ser um parâmetro recebido na chamada: 
# a. S = 2/500 - 5/490 + 2/480 - 5/470 +... 
# b. S=37*38/1 + 36*37/2 + 35*36/3 +...
def serbR (n, num=37, den=1):
    res = num * (num + 1) / den
    if n > 1:
        res = res + serbR (n - 1, num - 1, den + 1)
    else:
        res = - num * (num + 1) / den
    if n > 1:
        res = res + serbR (n-1, num -1, den +1)
    return res

def serb (n):
    return serbR(n)


############################ DIMINUIR CODIGO

def serbbR (n, num=37, den=1, s=1):
    res = s + num * (num + 1) / den
    if n > 1:
        res = res + serbbR (n-1, num -1, den + 1, -s)
    return res

def serbb (n):
    return serbbR(n)

############################
def serbbbR (n, num=37, den=1, s=1):
    res = s + num * (num + 1) / den
    print(res)
    if n > 1:
        print('Recursao>=: ', n-1, num -1, den + 1, -s)
        res = res + serbbbR (n-1, num -1, den + 1, -s)
    return res

def serbbb (n):
    return serbbbR(n)

num = int(input('Num: '))
while num > 0:
    print('Resultado = ', serbbb(num))
    num = int(input('num: '))


















