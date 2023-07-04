# Ler as notas finais de N alunos (N é informado pelo usuário antes), 
# calcular e imprimir a média destas notas e depois imprimir as notas que sejam maiores do que a média calculada.



n = int(input("Digite quantidade de notas: "))
notas = []
maior = []

for i in range(n):
    numero = float(input("Digite as notas: "))
    notas.append(numero)
media = sum(notas)/n 
for numero in notas:
    if numero > media:
        maior.append(numero)  
        print('nota maior que a media: ',maior)
print('sua media: ', media)

