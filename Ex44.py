print('{:=^40}'.format(' LOJAS MACEDO '))
v = float(input('Qual o preço do produto?'))
print('''OPÇÕES DE PAGAMENTO:
[ 1 ]  À vista dinheiro/cheque com 10% desconto
[ 2 ]  À vista no cartão com 5% desconto
[ 3 ]  2x no cartão
[ 4 ]  3x ou mais no cartão com 20% de juros''')

p = int(input('Qual a forma de pagamento?'))
if p == 1:
    total = v - (v*0.1)
elif p == 2:
    total = v - (v * 0.5)
elif p == 3:
    total = v
elif p == 4:
    total = v + (v*0.2)
else:
    print('Opção inválida de pagamento!')
print('Sua compra vai custar R${:.2f} no final.'.format(total))
