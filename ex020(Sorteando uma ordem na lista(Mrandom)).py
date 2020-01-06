import random
n1 = str(input('digite o primeiro grupo:'))
n2 = str(input('digite o segundo grupo:'))
n3 = str(input('digite o terceiro grupo:'))
n4 = str(input('digite o quarto grupo:'))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação será: \n',lista)

