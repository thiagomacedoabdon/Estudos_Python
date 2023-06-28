num = int(input('Digite um número inteiro: '))
print('''Escolha a base de conversão: 
[1] Binário
[2] Octal
[3] Hexadecimal''')
opcao = int(input('Sua opção foi: '))

if opcao == 1:
    print('O número {} em binário é {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} em octal é {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} em hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')