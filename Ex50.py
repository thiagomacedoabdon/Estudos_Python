soma = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        soma += n
print(f'O somatório de todos os valores pares é {soma}.')


