# Desvio Padrão
def variancia(valores):
    if len(valores) != 0:
        media = int(sum(valores)/len(valores))
    else:
        return "Não há valores para tratar"
    desvio = []
    for i in valores:
        dp = media - i
        desvio.append(dp)
    desvioElevado = []
    for i in desvio:
        desvioElevado.append(i**2)
    variancia = sum(desvioElevado)/len(desvioElevado)
    return variancia
    
def desvioPadrao(valores):
    dp = variancia(valores)**(1/2)
    return dp
    