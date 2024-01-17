import datetime
from time import sleep
# from scipy.stats import norm
                     
# Criei essa lista de problemas e quantidades para extrair o binomial da atividade, com essa lista vamos calcular
# qual chance de um problema especifico estar entre os próximos
problemas = {'Iluminacao': 12, 'Buraco': 15, 'Entulho': 13, 'Lixo': 17, 'Boca de lobo': 11, 'Outros': 10}
lista_problemas = []
for i in problemas.keys():
    lista_problemas.append(i)

def distBinomial(data):
    while True:
        try:
            with open("log.txt", "a") as novoLog:
                novoLog.write(f"Binomial Acessado {data}\n")
                print(f'\nOpções de Problema\n')
                for c, i in enumerate(lista_problemas):
                    print(f'{c + 1} - {i}')
                print("0 - Sair")
                
                opcaoRegistro = int(input("\nQual desses problemas gostaria de ver a probabilidade de ocorrer nos próximos registros: "))
                if opcaoRegistro < 0 or opcaoRegistro > len(lista_problemas):
                    print("\nValor inválido\n")
                    sleep(1)
                if opcaoRegistro == 0:
                    novoLog.write(f"Programa Fechado {data}\n")
                    print("\nFechando Programa...")
                    sleep(2)
                    exit()
                else:
                    novoRegistro = lista_problemas[opcaoRegistro - 1]
                    break
        except(ValueError):
            print("\nValor inválido\n")
            sleep(1)
    
    total = 0
    for i in problemas.values():
        total += i
            
    def fatorial(n):
        res = 1
        for i in range(1, n+1):
            res *= i
        return res
    
    n = 0 
    
    while True:
        try:          
            n = int(input(f"\nEm quantos registros(Amostras) você quer verificar a probabilidade do próximo registro ser {novoRegistro}: "))
            if n < 1 or n > total:
                print("\nValor inválido\n")
                sleep(1)
            else:                
                break
        except(ValueError):
            print("\nValor inválido\n")
            sleep(1)
    
    p = problemas[novoRegistro] / total
    lista_dist = []
    distFinalPerc = []
    opcao = 0
    
    tipos = ["de 0 a X valor", "de X valor a Y valor", "X valor", "X valor a último valor"]
    while True:
        print(f'\nOpções de k\n')
        for c, i in enumerate(tipos):
            print(f'{c + 1} - {i}')
        try:
            opcao = int(input("\nSelecione o valor do k que deseja usar: "))
            if opcao < 1 or opcao > n:
                print("\nValor inválido\n")
                sleep(1)
            else:
                break
        except(ValueError):
            print("\nValor Inválido\n")
            sleep(1)
    
    if opcao < 1 or opcao > n:
        print("Valor inválido")
    if opcao == 1:        
        menor_numero = 0
        maior_numero = int(input(f"\nQual quantidade no máximo deve ser encontrado na amostra: "))
    if opcao == 2:        
        menor_numero = int(input("\nQual quantidade no minimo a ser encontrado na amostra: "))
        maior_numero = int(input("\nQual quantidade no máximo a ser encontrado na amostra: "))
    if opcao == 3:        
        menor_numero = int(input("\nQual quantidade a ser encontrado na amostra: "))
        maior_numero = menor_numero
    if opcao == 4:        
        menor_numero = int(input("\nQual quantidade no minimo deve ser encontrado na amostra: "))
        maior_numero = n
        
    for k in range(menor_numero, maior_numero + 1):
        dist = fatorial(n)/(fatorial(k) * (fatorial(n - k)))
        dist_final = dist * (p**k * ((1 - p)**(n-k)))
        lista_dist.append(dist_final)
        distFinalPerc.append(dist_final * 100)
    sleep(1)

    linha = f' {"_" * 65}'
    print(f'\n{linha}\n{"Distribuição Binomial":>40}')    
    print(f'{linha}\n{"Distribuição":>45} {"Distribuição (%)":>20}\n{linha}')    
    for c, i in enumerate(lista_dist):
        print(f' Chance de Sucesso com K = {f"{menor_numero + c}"} {f"{i:.8f}":>15} {f"{distFinalPerc[c]:.2f}":>15}\n{linha}')
    print(f'\n TOTAL {f"{sum(lista_dist):.8f}":>38} {f"{sum(distFinalPerc):.2f}":>15}\n{linha}')
    
    # Função Binomial da Biblioteca de Python
    # binomial = sum(math.comb(n, i) 
    # probabilidade = sum(math.comb(n, i) * p**i * (1-p)**(n-i) for i in range(k+1)) * 100 
    # print(f'Distribuição Binomial = {probabilidade:.2f}%')
    
def distNormal():
    x = int(input("\nQual menos valor do desvio: "))
    media = int(input("\nQual a média das amostras: "))
    desvio = media - x
    dist_Nconf=norm.cdf(x, media, desvio)
    dist_Conf = 1-2*dist_Nconf
    print ('Valores conformes')
    print ('valor em decimal= ',dist_Conf)
    print ('valor em percentual',f'{dist_Conf:.2%}')
    print ('==================')
    print (f'Valores NÃO Conformes: {dist_Nconf*2:.2%}')
    print("Distribuição Normal")

    