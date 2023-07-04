'''
Q1- Faça uma subrotina Python do tipo função para calular a soma dos N primeiros termos da série
abaixo, onde o valor de N é um parâmetro e o resultado do cálculo da série é o resultado
da função

S = 2 -7/5 +8/3 -13/10 +32/9 -19/15 + 128/27 ...

Escrever também um programa principal para perguntar ao usuário a quantidade de vezes
(qtd) que ele deseja calcular o valor da série e, em seguida, os números desejados
nestas qtd vezes. Para cada um deles, seu programa deve usar
a função e imprimir o resultado da série (com 4 casas decimais), da seguinte
forma: 'O valor da série com ... termos é ...'.
'''


def serie(n):   # Normal, sem usar recursão
    num1 = 2
    den1 = 1
    num2 = 7
    den2 = 5
    resultado = 0.0
    
    for i in range(2, n+2):
        if i % 2 == 0:
            resultado = resultado + num1 / den1
            num1 = num1 * 4
            den1 = den1 * 3
        else:
            resultado = resultado - num2 / den2
            num2 = num2 + 6
            den2 = den2 + 5
    return resultado


n = int(input('Digite número de termos(<1 p/parar): '))
while n > 0:
    r1 = round(serie(n), 5)
    print(n, r1)
    n = int(input('Digite número de termos(<1 p/parar): '))
