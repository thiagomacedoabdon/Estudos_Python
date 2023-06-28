for c in range (1, 10): #FOR uso quando sei o limite
    print (c)


c = 1
while c<10: #WHILE quando não sei o limite, uso o while
    print(c)
    c+=1


n = 1
par = impar = 0
while n !=0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0: #resto da divisão
        par += 1
    else:
        impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')
