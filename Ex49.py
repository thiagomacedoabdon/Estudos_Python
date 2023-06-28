num = int(input('Escolha um número para mostrar a sua tabuada: '))
print ('{:=^20}'.format(' TABUADA '))
for n in range(1, 11):
    print('{} x {} = {}'.format(num, n, num*n))


