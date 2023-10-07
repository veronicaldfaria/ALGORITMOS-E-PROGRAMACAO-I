import math
x = 3.234
print(f'Valor original de x é {x}')
y = math.ceil(x)  # arredonda para cima
print (f'Valor arredondado de {x} para cima é {y}')
z = math.floor(x)  # arredonda para baixo
print (f'valor arredondado de {x} para baixo é {z}')
res1 = math.trunc(x)
print (f'Valor truncado de {x} é {res1}')
print (f'Parte inteira e parte fracionária de {x} é igual {math.modf(x)}')

a = -20
res = math.fabs(a) 
print (f'Valor absoluto de {a} é igual a {res}')





