import math
an = int(input('digite um angulo:'))
sen =math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O Seno de {}° é {:.2f}'.format(an,sen))
print('O cosseno de {}° é: {:.2f}'.format(an,cos))
print('A tangente d° {} é: {:.2f}'.format(an,tan))

