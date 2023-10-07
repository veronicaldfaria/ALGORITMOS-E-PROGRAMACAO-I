# Faça um programa em Python que, dada a idade de um atleta que será digitada pelo usuário,
# apresente a mensagem da coluna CATEGORIA de acordo com a tabela abaixo, onde a categoria
# depende da idade de entrada. Lembre-se de exibir a Categoria, exatamente como consta na tabela abaixo.

# CATEGORIA / IDADE
# NÃO TEM IDADE PARA SER ATLETA / Menor que 5
# INFANTIL A / 5 a 7
# INFANTIL B / 8 a 10
# JUVENIL A / 11 a 13
# JUVENIL B / 14 a 17
# SÊNIOR / Maior ou igual a 18

idade = int(input('Digite a idade: '))
if idade < 5:
    print('NÃO TEM IDADE PARA SER ATLETA')
elif idade >= 5 and idade <= 7:
    print('INFANTIL A')
elif idade >= 8 and idade <= 10:
    print('INFANTIL B')
elif idade >= 11 and idade <= 13:
    print('JUVENIL A')
elif idade >= 14 and idade <= 17:
    print('JUVENIL B')
elif idade >= 18:
    print('SÊNIOR')