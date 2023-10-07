import math
print ("Baskara")
a = float (input("A:"))
if a !=0:
    b = float (input("B:"))
    c = float (input("C:"))
    delta = math.pow(b,2)- 4 * a * c
    print(delta)
    if delta == 0 :
        x1 = (-b + math.sqrt(delta)) / (2*a)
        print ("Raiz : " , x1)
    elif delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f'Raizes : x1 = {x1} e x2 = {x2}')
        print(f'Simplificação {a}(x-{math.fabs(x1)})(x-{-x2})')
    else:
        print ("Não existem raizes reais")

else:
    print ("Não há equação do 2º grau")
