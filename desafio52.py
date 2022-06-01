from time import sleep
num = int(input('Digite um numero:'))
cont = 0
lista = []

print('\33[32mPara os numeros que podem ser divisíveis pelo numero digitado, '
      'a cor aparece em \033[33mamarelo \33[32me em \033[31mvermelho \33[32mos que não são divisíveis!!!')

sleep(1)


for c in range (1, num+1):

    if num % c == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{} -> '.format(c), end='')

if cont != 2:
    print('\n\n\33[31mO numero {} não é primo, pois é divisivel por {} numero(s).'.format(num, cont))

else:
    print('\n\nO numero {} é primo pois é divisivel por ele mesmo e por 1!'.format(num, c))




