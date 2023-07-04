check_valor = int(
    input("Digite o valor inteiro do salário que você quer imprimir: "))
nome_arquivo = str(input(
    "Digite o nome do arquivo de saída para a faixa de salário selecionada: "))
soma_homem, qtd_homem = 0
soma_mulher, qtd_mulher = 0

ent = open(nome_arquivo, 'r')
sai = open('C:\python\teste.txt', 'w')

for i in ent:
    matricula = i[0:5]
    sexo = i[6]
    nome = i[7:37]
    salario = i[38:48]

    if (salario >= check_valor):
        if (sexo == 1):
            soma_homem += salario
            qtd_homem += 1
        else:
            soma_mulher += salario
            qtd_mulher += 1
        sai.write('%s \t %s' % (matricula, salario))
ent.close()
sai.close()

print("Número de registros gravados no arquivo: " + str(qtd_homem+qtd_mulher))
print("Média de salário masculino: " + str(soma_homem/qtd_homem))
print("Média de salário feminino: " + str(soma_mulher/qtd_mulher))
