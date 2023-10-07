# Faça um programa em Python que receba o custo (valor em reais) de um
# espetáculo teatral e o preço do convite (valor em reais) desse espetáculo.
# Esse programa deve calcular e mostrar, nesta ordem:
# a) A quantidade de convites que devem ser vendidos para que pelo menos o
# custo do espetáculo seja alcançado.
# b) A quantidade de convites que devem ser vendidos para que se tenha um
# lucro de 23%.
# Observe que as quantidades calculadas a serem vendidas devem ser um número
# inteiro; portanto, o resultado da quantidade de convites deve ser arredondado
# para cima, usando a função matemática apropriada em Python.

import math
valortotal = float(input())
valorconvites = float(input())
qtdconvites1 = valortotal / valorconvites
qtdconvites1pracima = math.ceil(qtdconvites1)
print(qtdconvites1pracima)
valortotalcomlucro = (123 * valortotal) / 100
qtdconvites2 = valortotalcomlucro / valorconvites
qtdconvites2pracima = math.ceil(qtdconvites2)
print(qtdconvites2pracima)