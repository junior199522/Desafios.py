num = int(input('Digite um numero:'))
res = int(input('Escolha uma das bases de conversão: \n[ 1 ] Converter para BINARIO \n[ 2 ] Converter para OCTAL \n[ 3 ] Converter para HEXADECIMAL \nSua opção:'))
if res == 1:
    print(format(num, "b"))
elif res == 2:
    print(format(num, "o"))
elif res == 3:
    print(format(num, "x"))
else:
    print('Programa encerrado, voce digitou algo diferente de 1, 2 ou 3!')