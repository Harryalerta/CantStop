import modulos.calculadorProbabilidade

valores_a_calcular = [2,12,3]
dados = [1,1,1,1]
dados_anterior = []
validos = 0
invalidos = 0

while dados_anterior != dados:
    dados_anterior = dados.copy()
    if modulos.calculadorProbabilidade.verifica_combinacao(dados, valores_a_calcular):
        validos += 1
    else:
        invalidos += 1
    dados = modulos.calculadorProbabilidade.proximo_do_arranjo(dados)

print("Válidos: " + str(validos))
print("Inválidos: " + str(invalidos))

print("Chance: " + str(validos/(validos+invalidos)))
