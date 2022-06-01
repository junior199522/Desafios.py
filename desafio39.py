from datetime import  date
ano = date.today().year
nasc = int(input('Em qual ano voce nasceu?'))

if ano - nasc <= 17:
    print('Ainda falta {} ano(s) para voce se alistar voce narceu em {}, o seu ano de alistamento é {}!'.format(18 - (ano - nasc), nasc, nasc+18))
elif ano - nasc == 18:
    print('Esse é seu ano de se alistar, voce tem ou vai fazer 18 anos')
elif ano - nasc > 18:
    print('Voce nasceu em {}, passou do seu ano de alistamento, e esta a {} ano(s) atrasado, sua idade é {} anos, seu ano de alistamento foi {}'.format(nasc, (ano - nasc) - 18,  ano - nasc, nasc +18) )

