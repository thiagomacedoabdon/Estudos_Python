from datetime import date
nascimento = int(input('Qual o seu ano de nascimento: '))
idade = date.today().year - nascimento
if idade == 18:
    print('Chegou a hora de se alistar no serviço militar!')
elif idade < 18:
    print('Ainda falta algum tempo para se alistar!')
else:
    print('Ja passou da idade do alistamento! Aconselhamos faze-lo imediatamente!')
