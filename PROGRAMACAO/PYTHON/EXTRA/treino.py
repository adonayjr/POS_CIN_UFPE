import math

x = 144
y = 2

print(pow(x, y))
print(round(x, 2))

print(math.sqrt(x))
print(math.pi)
print(math.trunc(x))
print(math.floor(x))
print(math.ceil(x))
print(math.sin(x))


soma = 0
for i in range(1, 3+1):  # 51 é 50 + 1 e passo é 1.
    soma = soma + i  # No final i estará com 50.
print(soma)


soma = 0
i = 1
while i <= 50:  # Note que aqui i estará com 51 após terminar...
    soma = soma + i
    i = i + 1
    print(i)


