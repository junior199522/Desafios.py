peso = float(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura?'))

imc = peso / (altura * altura)

if imc < 18.50:
    print('Voce está abaixo do peso.')
elif imc >= 18.50 and imc < 25:
    print('Voce está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Voce está com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Voce está com obesidade.')
else:
    print('Voce está com Obesidade Mórbida')


print('Seu IMC é {:.1f}'.format(imc))