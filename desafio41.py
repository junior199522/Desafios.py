from datetime import date
ano = date.today().year
nasc = int(input('Em qual ano voce nasceu?'))
idade = ano - nasc

if idade <= 9:
    print('Voce tem {} anos. \nClassificação: Mirim'.format(idade))
elif idade <=14:
    print('Voce tem {} anos. \nClassificação: Infantil'.format(idade))
elif idade <=19:
    print('Voce tem {} anos. \nClassificação: Junior'.format(idade))
elif idade <=25:
    print('Voce tem {} anos. \nClassificação: Senior'.format(idade))
elif idade >25:
    print("Voce tem {} anos. \nClassificação: Master".format(idade))