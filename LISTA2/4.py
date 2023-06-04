# Ler o nome completo do usuário e imprimi-lo com o primeiro e último nome escritos todo em maiúsculas.

usuario = input("Digite seu nome de usuario: ")

web1 = usuario.split (' ')
print(web1)

web1[0] = web1[0].upper() 
web1[-1] = web1[-1].upper() 
juntar = " ".join(web1)

print(juntar)