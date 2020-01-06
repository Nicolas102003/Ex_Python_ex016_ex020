import random
n1 = str(input('digite o primeiro nome :'))
n2 = str(input('digite o segundo nome :'))
n3 = str(input('digite o terceiro nome :'))
n4 = str(input('digite o quato nome :'))
array = [n1,n2,n3,n4]
nome = random.choice(array)
print('o aluno escolhido foi: {}'.format(nome))

