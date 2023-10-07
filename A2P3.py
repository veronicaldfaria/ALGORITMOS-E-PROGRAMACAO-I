# Faça um programa em Python que resolva o seguinte problema:
# Um concurso possui um prêmio no montante de R$ 780.000,00 para
# dividir entre três ganhadores da seguinte forma:
# - o primeiro ganhador receberá 46% do prêmio;
# - o segundo ganhador receberá 32% do prêmio;
# - o terceiro receberá o restante do prêmio.
# Calcule e mostre o valor do prêmio de cada ganhador, nesta ordem:
# primeiro colocado, segundo colocado e terceiro colocado.
# Observe que este programa não tem valor de entrada feita pelo usuário.

valortotal = 780000
ganhador1 = (46 * valortotal) / 100
print(ganhador1)
ganhador2 = (32 * valortotal) / 100
print(ganhador2)
ganhador3 = (((100 - 46 - 32) * valortotal) / 100)
print(ganhador3)