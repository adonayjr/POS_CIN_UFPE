# 1) Considere um arquivo texto cujo nome externo é “discip.old" que contém informações de disciplinas
# (Código com 5 posições, nome com 35 posições e créditos com 2 posições), uma disciplina por linha.
# Seu programa deve criar um segundo arquivo com nome externo “discip.new" contendo informações das mesmas disciplinas,
# mas com as seguintes modificações:
# (a) As disciplinas cujos códigos são IF125 e IF380 devem ser excluídas, i.e.,não devem ser gravadas no novo arquivo.
# (b) Os números de créditos das disciplinas cujos códigos começam por MA devem ser alterados para 5.
# (c) O novo arquivo terá um campo a mais (carga horária, com 3 posições) cujo valor deve ser o número de créditos
# da disciplina multiplicado por 15.
# No final o seu programa deve imprimir o número de disciplinas de cada arquivo e
# ainda o número de disciplinas que tiveram seus números de créditos alterados.

# Testa arquivos texto básicos de entrada e saída
tab = {}

cod = int(input('cod.curso: '))

while (cod <= 0):
    cod = int(input('invalido cod.curso: '))

while cod != 0:
    nome = input('nome.curso: ')
    ccen = int(input('cod.centro: '))
    while ccen <= 0:
        ccen = int(input('invalido. cod.centro: '))
    tab[cod] = (nome, ccen)

    cod = int(input('cod.curso: '))
    while (cod < 0) or (cod in tab):
        cod = int(input('invalido. cod.curso: '))
print(tab)

ccen = int(input('cod.centro: '))
while ccen <= 0:
    ccen = int(input('invalido. cod.centro: '))

while ccen > 0:
    qtd = 0
    print('curso do centro', ccen)
    for cod in tab:
        if ccen == tab[cod][1]:
            print(cod, tab[cod][0])
            qtd = qtd + 1
    if qtd == 0:
        print('nenhum curso encontrado')

    ccen = int(input('cod.centro: '))
