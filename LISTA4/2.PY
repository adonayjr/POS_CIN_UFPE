# Achar todos os números palindromos existentes entre 100 e 5000. 
# Um número é palindromo se ele tiver o mesmo valor quando escrito da direita para a esquerda. 
# Ex: 17371. Escreva e utilize uma subrotina cujo resultado é o valor recebido no parâmetro (numero inteiro) 
# escrito ao contrário. 



def inverter (n):
    res = 0
    while n > 0:
        res = res * 10 + (n % 10)
        n = n // 10
    return res

for i in range (10000, 19500):
    if i == inverter (i):
        print(i, end=' ')
print('Fim')