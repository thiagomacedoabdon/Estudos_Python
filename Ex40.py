n1 = float(input('Qual a nota da primeira prova:'))
n2 = float(input('Qual a nota da segunda prova:'))
media = (n1 + n2) / 2

if media < 5.0:
    print('Reprovado!')
elif 6.9 >= media >= 5.0:
    print('Recuperação!')
else:
    print('Aprovado!')