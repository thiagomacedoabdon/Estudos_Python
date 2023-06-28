print('Gerar PA')
print('==='*10)

p = int(input('Primeiro termo:'))
razão = int(input('Razão da PA:'))
termo = p
cont = 1

while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razão
    cont += 1
print('FIM')

