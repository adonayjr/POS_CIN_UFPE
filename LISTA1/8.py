inicio = int(input("Digite o valor de início (em Fahrenheit): "))
fim = int(input("Digite o valor de fim (em Fahrenheit): "))

print("Tabela de Conversão de Fahrenheit para Celsius")
print("--------------------------------------------")
print("Fahrenheit \t Celsius")

for fahrenheit in range(inicio, fim + 1):
    celsius = (fahrenheit - 32) * 5/9
    print(fahrenheit, "\t\t", round(celsius, 2))

###################################################################################
inicio = int(input("Digite o valor de início (em Fahrenheit): "))
fim = int(input("Digite o valor de fim (em Fahrenheit): "))

print("Tabela de Conversão de Fahrenheit para Celsius")
print("--------------------------------------------")
print("Fahrenheit \t Celsius")

fahrenheit = inicio

while fahrenheit <= fim:
    celsius = (fahrenheit - 32) * 5/9
    print(fahrenheit, "\t\t", round(celsius, 2))
    fahrenheit += 1