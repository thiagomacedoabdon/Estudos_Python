p = float(input('Qual o seu peso (Kg)?'))
a = float(input('Qual a sua altura (m)?'))
imc = p/(a**2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))

if imc < 18.5:
    print('Está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Está com o peso ideal!')
elif 25 <= imc < 30:
    print('Está com sobrepeso!')
elif 30 <= imc < 40:
    print('Está com obesidade!')
else:
    print('Está com obesidade morbida!!!')