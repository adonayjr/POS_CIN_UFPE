# S = 1 - 3/5 + 5/2 - 7/8 + 9/3 - 11/11
def ser (n):
    num = 1
    de1 = 1
    de2 = 5
    res = 0.0

    for i in range(n):
        if i % 2 == 0:
            res = res + num / de1
            de1 = de1 + 1
        else:
            res = res - num / de2
            de2 = de2 + 3
        num = num + 2
    return res

def serR (n, num=1, de1=1, de2=5, sin=1):
    if sin == 1:
        res = num / de1
    else:
        res = - num / de2
    if n > 1 :
        if sin == 1:
            res  = res + serR (n-1, num+2, de1+1, de2, -1)
        else:
            res = res + serR (n-1, num+2, de1, de2+3, 1)
    return res

n = int(input('Digite número de termos(<1 p/parar): '))
while n > 0 :
    r1 = round(ser(n), 5)
    r2 = round(serR(n), 5)
    print (n, r1, r2)
    n = int(input('Digite número de termos(<1 p/parar): '))