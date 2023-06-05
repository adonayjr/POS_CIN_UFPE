# Ler 2 vetores de tamanho N, com N informado pelo usuário antes, somar os 2 vetores, 
# imprimir os 2 vetores e depois o vetor resultado.
                                         
vet1 = int(input('N1: '))
vet2 = int(input('N2: '))

lista = []

lista.append (vet1)
lista.append (vet2)

soma = lista[0] + lista[1]

print(lista, lista[0], "+", lista[1], "=", soma)