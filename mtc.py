# Média
def media(dados):
    media = sum(dados)/len(dados)    
    return f'Temos uma média de {int(media)}'
    
# Mediana
def mediana(dados):    
    m = len(dados) / 2
    mediana = 0

    if len(dados) % 2 == 0:
        mediana = (dados[int(m - 1)] + dados[int(m)]) / 2
        
    else:
        mediana = dados[int(len(dados) * 0.5)]
        
    return f'A mediana é de {mediana:.2f}'
    
# Primeiro Quartil
def quartil1(dados):
    meio = len(dados) // 2
    # separa a dados nos primeiros quartis
    if len(dados) % 2 == 0:
        quartil1e2 = dados[:meio]
    else:
        quartil1e2 = dados[:meio]
    
    # calcula o primeiro quartil
    quartil1 = len(quartil1e2) // 2
    if len(quartil1e2) % 2 == 0:
        q1 = (quartil1e2[quartil1 - 1] + quartil1e2[quartil1]) / 2
    else:
        q1 = quartil1e2[quartil1]
        
     #Imprime a resposta
    return f'O Primeiro Quartil é {q1:.2f}\n'
    
# Terceiro Quartil
def quartil3(dados):
    meio = len(dados) // 2
    # separa a dados nos ultimos quartis
    if len(dados) % 2 == 0:
        quartil3e4 = dados[meio:]
    else:
        quartil3e4 = dados[meio + 1:]
    
    # calcula o terceiro quartil
    quartil3 = len(quartil3e4) // 2
    if len(quartil3e4) % 2 == 0:
        q3 = (quartil3e4[quartil3 - 1] + quartil3e4[quartil3]) / 2
    else:
        q3 = quartil3e4[quartil3]
        
    #Imprime a resposta
    return f'O Terceiro Quartil é {q3:.2f}\n'
    
# Função para encontrar a Moda    
def moda(dados):
    
    repeticoes = []
    moda = []
            
    # Adcionando o número de repetições de cada dado em uma lista
    for i in dados:
        repeticoes.append(dados.count(i))
        
    repeticoes = sorted(repeticoes)

    # Pegando somente os valores que mais se repetem
    for i in dados:
        if dados.count(i) == repeticoes[-1]:
            if repeticoes[-1] != 1:
                if i not in moda:
                    moda.append(i)
                    
    # Imprimindo a Moda   
    if moda == []:        
        return "Não há valores repetidos"
    else:
        return f'Houveram {moda} registros em {repeticoes[-1]} dias diferentes na semana'