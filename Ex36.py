from time import sleep
valor = float(input('Qual o valor necessário para comprar a casa?'))
salario = float(input('Qual o rendimento total do comprador?'))
prazo = int(input('Qual o prazo necessário para o financiamento em meses?'))
ValorParcela = valor / prazo

print('PROCESSANDO...')
sleep(0.5)

if ValorParcela >= salario * 0.3:
    print('Sentimos muito! Mais o valor da parcela ultrapassa os 30% de margem salarial.')

else:
    print('Parabéns! Você acaba de ter o empréstimo aprovado!')
    print('O valor da parcela será de {:.2f}'.format(ValorParcela))


