n1 = float(input('Digite um numero:'))
n2 = float(input('Digite outro numero:'))

if n1 > n2:
    print('O primeiro numero digitado {:.2f} é maior que o segundo numero digitado {:.2f}!'.format(n1, n2))
elif n2 > n1:
    print('O segundo numero digitado {:.2f} é maior que o primeiro numero digitado {:.2f}!'.format(n2,n1))
else:
    print('Os numeros {:.2f} e {:.2f} são iguais'.format(n1, n2))

