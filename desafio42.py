n1 = float(input('Qual o tamanho da primeira reta?'))
n2 = float(input('Qual o tamanho da segunda reta?'))
n3 = float(input('Qual o tamanho da terceira reta?'))
base = float
soma = float

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Com as retas digitadas: \nReta 1: {:.2f} \nReta 2: {:.2f} \nReta 3: {:.2f} \nConseguimos fazer um triangulo!!!'.format(n1, n2, n3))

    if n1 == n2 == n3:
        print('Esse é um triangulo EQUILÁTERO: Todos os seus lados são iguais.')

    elif n1 != n2 != n3 != n1:
        print('Esse é um triangulo ESCALENO: Todos os lados diferentes.')

    else:
        print('Esse é um triangulo ISÓSCELES: dois lados iguais, um diferente')

else:
    print('Com as retas digitadas: \nReta 1: {:.2f} \nReta 2: {:.2f} \nReta 3: {:.2f} \nNão conseguimos fazer um triangulo!!! '
          '\nPois as duas menores retas somadas, não foi superior a maior reta!'.format(n1,n2,n3))