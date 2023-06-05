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
nomeArqEnt = input ('Digite o nome do arquivo: '')
try :
arqEnt = open (nomeArqEnt)
arqSai = open ('C://Python27/veicVelhos.txt', 'w')
numVeic = 0
for line in arqEnt :

placa = line[0:7]
marca = line[8:13]
modelo = line[14:22]
ano = int(line[23:27])
cpf = line[28:39]
if ano <= 2000 :
arqSai.write('%s %d %s\n' % (placa, ano, cpf) )
numVeic = numVeic + 1