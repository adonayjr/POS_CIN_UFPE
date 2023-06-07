# 3. Ler uma tabela de alunos onde: e Cada aluno tem um cpf (inteiro), um nome (String) e uma idade (inteiro).
# e Aleitura da tabela pára com um cpf que não seja positivo. e Sabe-se que o usuário digitará no máximo 200 alunos.
# e Depois o usuário informará um inteiro positivo N,
# seguido por uma série de N intervalos de idade (idades mínima e máxima).
# e O programa deve imprimir, para cada intervalo digitado pelo usuário,
# os dados dos alunos que se enquadram no intervalo seguidos pelo número de alunos do intervalo.
# e Caso a idade mínima de algum intervalo não seja menor do que a idade máxima,
# O programa deve imprimir uma mensagem de erro e continuar. 


tab = {}
qtd = 0

cpf = int(input('CPF: '))
while cpf > 0:
    qtd = qtd + 1
    nome = input('nome: ')
    idade = float(input('idade: '))
    tab[cpf] = (nome, idade)
    cpf = int(input('CPF: '))
if cpf > 0:
    print('Qtd maxima atingida')
print(tab)

n = int(input('N: '))
while n < 1:
    n = int(input('invalido. n: '))

for i in range(n):
    min = int(input('idade min: '))
    while min < 1:
        min = int(input('invalida. idade minima: '))
    max = int(input('idade maxima: '))
    while max < 1:
        max = int(input('invalida. iidade max: '))
    if min > max:
        print('Intervalo invalido ignorado')
    else:
        qtd2 = 0
        for cpf in tab:
            nome, idade = tab[cpf]
            if min <= idade and idade <= max:
                print(cpf, nome, idade)
                qt2 = qtd2 + 1
        print(qt2, 'alunos selecionados')
