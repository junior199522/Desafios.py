compras = float(input('Qual o valor das compras?'))
pagar = int(input('Formas de pagamento: \n[ 1 ] Á vista dinheiro/cheque. \n[ 2 ] A vista cartão. \n[ 3 ] 2x mo cartão. \n[ 4 ] 3x ou mais no cartão\n'))

if  pagar == 1:
    print('O valor é R${:.2f}, mas com 10% de desconto por pagar a vista ou cheque ficou R${:.2f}'.format(compras, compras - (compras * 10 / 100)))
elif pagar == 2:
    print('O valor é R${:.2f}, mas com 5% de desconto por pagar no cartão a vista ficou R${:.2f}'.format(compras, compras - (compras * 5 / 100)))
elif pagar == 3:
    print('O valor é R${:.2f} e em até 2x no cartão não sofre alteração.'.format(compras))
elif pagar == 4:
    print('O valor é R${:.2f} e por parcelar em 3x ou mais sofre um aumento de 20% totalizando R${:.2f}'.format(compras, compras + (compras * 20 / 100)))
else:
    print('Opção de pagamento invalida!!!')


