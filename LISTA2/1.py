# Ler o nome do usuário e imprimi-lo na vertical, ou seja, uma letra embaixo da outra.

def new_func():
    nome = input("Digite seu nome: ")


    for i in list(nome):
        
        print(i)

new_func()


#####################################

def new_func():
    nome = input("Digite seu nome: ")


    for i in range(len(nome)):
        
        print("%d - %s" % ((i + 1), nome[i]))

new_func()