# Ler 2 strings e dizer quantas vezes o primeiro aparece no segundo 


def new_func():
    string = input("Digite a string: ")
    sub = input("Digite a sub: ")

    pos1 = string.find(sub)

    print('Quantas vezes a sub aparece na string', pos1)

new_func()

