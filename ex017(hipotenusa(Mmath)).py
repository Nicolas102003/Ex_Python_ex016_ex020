import math
a = float(input('digite o valor do cateteto oposto:'))
b = float(input('digite o  valor do cateto adjacente:'))
hi = (math.pow(a,2) + math.pow(b,2))
hi = math.sqrt(hi)
print('a hipotenusa vai medir: {:.2f}'.format(hi))