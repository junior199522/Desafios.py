soma = 0
cont = 0
for c in range(0, 6):
    a = int(input('Digite um numero inteiro: '))
    if a % 2 == 0:
        soma += a
        cont += 1
print('A soma dos {} numeros pares é {}!!!'.format(cont, soma))

