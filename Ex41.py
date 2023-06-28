from datetime import date
ano = int(input('Qual o ano de nascimento do(a) atleta?'))
idade = date.today().year - ano

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')