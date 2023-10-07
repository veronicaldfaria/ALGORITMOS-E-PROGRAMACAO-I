#divisão de conta entre 3 amigos, onde 1 deles vai pagar os centavos
valor= float(input('Valor da conta:'))
divisao = valor/3
cada = int(divisao)
sobra = valor - 2 * cada
print('Carlos irá pagar R$ %.4f '  %cada)
print('André irá pagar R$ %.2f '  %cada)
print('Felipe irá pagar R$ %.2f ' %sobra)




