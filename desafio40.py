n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2
if media >= 7:
    print('Parabens voce foi APROVADO, sua media foi: {}'.format(media))
elif media >=5:
    print('Voce está de RECUPERAÇÃO, sua media foi {}, e precisava de 7 para passar sem recuperação:'.format(media))
elif media <5:
    print('Voce está REPROVADO sua media foi: {}'.format(media))