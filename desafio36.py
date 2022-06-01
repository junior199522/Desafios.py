casa = float(input('Qual o valor da casa que pretende comprar?'))
sal = float(input('Qual o valor do seu salario?'))
ano = int(input('Em quantos anos vai pagar a casa?'))
meses = ano*12
porc = (sal * 30 / 100)

if porc > casa/meses:
    print('Para pagar uma casa de {:.2f} em {} anos, a parcela sera de r${:.2f}. \nEmprestimo concedido!!!'.format(casa, ano, casa/meses))

else:
    print('Para pagar uma casa de {:.2f} em {} anos, a parcela sera de {:.2f}. \nEmprestimo negado!!!'.format(casa, ano, casa/meses))
