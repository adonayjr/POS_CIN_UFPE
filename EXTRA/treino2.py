nomeArqEnt = input ('Digite o nome do arquivo: ')
try :
    arqEnt = open (nomeArqEnt, 'r')
    arqSai = open ('C://python/teste.txt', 'w')
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
    print ('Número de veículos gravados =', numVeic)
    arqEnt.close()
    arqSai.close()
except IOError as mens:
    print ('ERRO em arquivo: ', mens)
except :
    print ('ERRO: Outros')

print ('Fim de Programa!')
