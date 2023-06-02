# 1. Ler uma tabela com Cursos, onde: e Cada curso é formado por um código (inteiro positivo), um nome (String), e o centro a que pertence (inteiro positivo). A leitura da tabela de cursos pára com o código de curso zero. Depois o usuário fornecerá uma lista de códigos de centro para que o programa imprima o código e nome de todos os cursos associados a cada centro digitado. Se o código do centro não existir na tabela, mostrar a mensagem “Nenhum curso encontrado” e continuar. O programa pára com a digitação de um código de centro inválido (negativo ou zero). 

def new_func():
    n = int(input ('Digite o tamanho da tabela de profissões: '))

    while (n < 1) :
        n = int(input ('Tamanho deve ser inteiro e positivo. Tente novamente: '))
    tab = { } # Criação do dicionário...

    for i in range (n) :
        codP = int(input ('Digite o código de uma profissão: '))

        while (codP < 1) :
            codP = int(input ('Código deve ser inteiro e positivo. Tente novamente: '))
        nomeP = input ('Digite o nome da profissão %d:\n' % (codP))
        areaP = input ('Digite a área da profissão %d:\n' % (codP))
        tab [codP] = (nomeP, areaP) # Inserção no dicionário...

    print ('Tabela com %d profissões foi lida corretamente.' % (n))
    print ('Tabela ->', tab)
    codP = int(input ('Digite um código de profissão para busca (<=0 para parar): '))

    while codP > 0 :
        if codP in tab : # Verifica se a profissão existe na tabela...
            nomeP, areaP = tab[codP] # Recupera os outros dados...
            print ('Profissão %d é %s e sua área é %s.' % (codP, nomeP, areaP))
        else:
            print ('Profissão %d não existe na tabela.' % (codP))
        codP = int(input ('Digite outro código para busca (<=0 para parar): '))

    print ('Fim de Programa')

new_func()


                 