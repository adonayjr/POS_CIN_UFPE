# Ler o nome completo do usuário e imprimi-lo com o primeiro e último nome escritos todo em maiúsculas.

usuario = input("Digite seu nome de usuario: ")

separar = usuario.split (' ')
print('Lista com seu nome: ', separar)

separar[0] = separar[0].upper() 
separar[-1] = separar[-1].upper() 
juntar = " ".join(separar)

print('Primeiro e ultimo nome maiusculo', juntar)