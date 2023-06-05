# Altere o programa anterior para garantir que o usuário digitará no máximo 1000 números. 

maximo = 5
lista = [0] *maximo
cont = 0
cont2 = 0

num = int(input("numero :"))
while num < 0:
    num = int(input("invalido. n: "))

while num >= 0 and cont < 5:
    cont = cont + 1
    if num > 9 and num < 100:
        lista[cont2] = num
        cont2 = cont2 + 1
    num = int(input("numero: "))

if num >= 0:
    print('Maximo atingido')
if cont == 0:
    print('Nenhum numero de 2 digitos')
else:
    for i in range (cont2 -1, -1, -1):
        print(lista[i])
print(lista)