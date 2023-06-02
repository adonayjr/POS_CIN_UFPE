# Leitura dos dois números inteiros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Cálculo do resto da divisão
resto = numero1 % numero2

# Verificação do resultado
if resto == 0:
    print("O resto da divisão é zero.")
    print("Primeiro número:", numero1)
else:
    print("O resto da divisão não é zero.")
    print("Quadrado do resto:", resto ** 2)
