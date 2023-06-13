# Q3 — Faça uma subrotina Python do tipo Procedimento chamada MelhoresClientes para:
# (a) ler um arquivo texto cujo nome externo é formado a partir do nome de uma empresa, recebido como parâmetro,
# seguido da extensão 'txt'. O arquivo conterá as informações dos clientes do programa de fidelidade desta empresa,
# a saber: matricula (inteiro com 5 dígitos), sexo (l=masculino ou 2=feminino), número de pontos (inteiro com 7 dígitos),
# e nome do cliente (string com 35 posições). Arquivo exemplo será fornecido juntamente com a questão.

# (b) Gravar um arquivo, cujo nome externo é 'Melhores' concatenado após o nome da empresa,
# seguido da extensão '.txt', contendo somente a matrícula e o total de pontos (um cliente por linha)
# dos clientes com pontuação acima de um dado valor recebido como segundo parâmetro na subrotina.
# Ou seja, este procedimento deve ter 2 parâmetros.

# (c) No final, o procedimento deve imprimir (na tela do terminal) um resumo das informações
# gravadas no arquivo contendo o nome da empresa, o número de registros gravados no arquivo
# e a média das pontuações destes melhores clientes.

# Faça também um programa principal que leia o nome da empresa e o total de pontos a ser considerado
# na escolha dos melhores clientes de N empresas, com N informado no início pelo usuário,
# e faça uso do procedimento MelhoresClientes para cada uma delas.
# Caso ocorra erro no arquivo de alguma das empresas, o seu programa deve informar o usuário e desconsiderar esta empresa,
# possivelmente continuando a executar com outras empresas. ------------------ Valor da questão: 4,5

def MelhoresClientes(empr, base):
    media = 0.0
    grav = 0
    nomeArqEnt = 'D:\\' + empr + '.txt'
    nomeArqSai = 'D:\\' + empr + 'Melhores.txt'
    arqEnt = open(nomeArqEnt, 'r')
    arqSai = open(nomeArqSai, 'w')

    for linha in arqEnt:
        matr = linha[0:5]
        sexo = linha[6]
        pontSt = linha[8:15]
        pontos = int(pontSt)
        nomeC = linha[16:51]

        if pontos > base:
            arqSai.write('%s %s\n' % (matr, pontSt))
            media = media + pontos
            grav = grav + 1

    arqEnt.close()
    arqSai.close()
    print('Gravado arq. da empresa', empr, 'com cli. acima', base, 'pontos.')

    if grav > 0:
        media = media / grav
        print('   Selec.', grav, 'clientes, com média de', media, 'pontos.')
    else:
        print('   Nenhum cliente selecionado.')

    return   # Comando opcional


n = int(input('Digite o número (>0) de empresas a processar: '))
while n < 1:
    n = int(input('Digite o número (>0) de empresas a processar: '))

for i in range(n):
    nome = input('Digite o nome da empresa: ')
    pont = int(input('Digite a pontuação base (>=0) a ser usada: '))
    while pont < 0:
        pont = int(input('Digite a pontuação base (>=0) a ser usada: '))

    try:
        MelhoresClientes(nome, pont)
    except IOError:
        print('Erro no arquivo da empresa', nome, ': empresa desprezada.')

print('Fim do programa')
