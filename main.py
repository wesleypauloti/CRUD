from datetime import datetime
from time import sleep
import mtc
import MedidasVar
import crud
import Distribuicao

dados = []
path = "CRUD/dados.txt"
sair = False
while sair == False:
    try:
        with open(path, "r") as arquivo:
            for i in arquivo:
                dados.append(i.rstrip().split(","))
        if dados == []:
            print("\nNão há dados para analisar")
            path = input("\nTente novamente ou digite [Sair] para encerrar: ").lower()
            if path == "sair":
                sair = True
                print("\nObrigado, volte Sempre!\n")
                exit()
        else:
            break   
    except(FileNotFoundError):
        print("Caminho do arquivo está incorreto")
        path = input("\nTente novamente ou digite [Sair] para encerrar: ").lower()
        if path == "sair":
            sair = True
            print("\nObrigado, volte Sempre!\n")
            exit()
valores = {}
listaValores = []
quantidade = []

log = []
data = datetime.now().strftime('%d/%m/%Y %H:%M')

for i in dados:
    valores["Dia"] = (i[0])
    valores["Quantidade"] = (i[1])
    listaValores.append(valores)
    quantidade.append(int(i[1]))
    valores = {}
    
def opcoes():
    print(f"\n{'OPÇÕES':>20}\n")
    opcoes = ["Visualizar Registros", "Alterar", "Incluir", "Excluir", "Produzir Relatórios"]
    for c, i in enumerate(opcoes):
        print(f'{c + 1} - {i}')
    print("0 - Sair")
    
def opcoes_iniciais():
    opcoes_iniciais = ["CRUD", "Distribuição", "LOG"]
    print(f"\n{'OPÇÕES':>20}\n")
    for c, i in enumerate(opcoes_iniciais):
        print(f'{c + 1} - {i}')
    print("0 - Sair")

def OpcoesDist():
    print(f"\n{'OPÇÕES DE DISTRIBUIÇÃO':>20}\n")
    opcoes = ["Distribuição Binomial", "Distribuição Normal"]
    for c, i in enumerate(opcoes):
        print(f'{c + 1} - {i}')
    print("0 - Sair")
    
    while True:
        try:
            with open("log.txt", "a") as novoLog:    
                opcao = int(input("\nQual operação gostaria de executar: "))                                    
                if opcao < 0 or opcao > 2:
                    print("\nValor Inválido\n")
                    sleep(1)
                if opcao == 1:
                    novoLog.write(f"Distribuicao Binomial Acessada {data}\n")
                    print("\nAcessando Distribuiçaõ Binomial...")
                    sleep(1)
                    Distribuicao.distBinomial(data)
                    sleep(2)
                if opcao == 2:
                    novoLog.write(f"Distribuicao Normal Acessada {data}\n")
                    print("\nAcessando Distribuiçaõ Normal...")
                    sleep(1)
                    Distribuicao.distNormal()
                    sleep(2)
                if opcao == 0:
                    novoLog.write(f"Programa Fechado {data}\n")
                    print("\nFechando Programa...")
                    sleep(2)
                    exit()        
        except(ValueError):
            print("\nValor Inválido\n")
            sleep(1)

def editar_log():
    log = []
    with open("log.txt", "r") as logs:
        for i in logs:
            log.append(i.rstrip())
    print()
    for c, i in enumerate(log):
        print(f'{c + 1} - {i}')

    while True:
        try:
            with open("log.txt", "a") as novoLog:
                linha = int(input("\nQual linha gostaria de Excluir ou digite 0 para excluir tudo: "))
                print()
                if linha < 0 or linha > len(log):
                    print("\nValor Inválido\n")
                    sleep(1)
                if linha == 0:                
                    with open("log.txt", "w") as novoLog:
                        novoLog.write('')
                    print("Excluido com Sucesso!\n")
                    break 
                if linha > 0 and linha <= len(log):
                    log.pop(linha - 1)
                    with open("log.txt", "w") as novoLog:
                        for i in log:
                            novoLog.write(f'{i}\n')
                    print("Excluido com Sucesso!\n")
                    break                
        except(ValueError):
            print("Valor inválido")

while True:
    try:
        with open("log.txt", "a") as novoLog:
            opcoes_iniciais()       
            opcao = int(input("\nQual operação gostaria de executar: "))                                    
            if opcao < 0 or opcao > 3:
                print("\nValor Inválido\n")
                sleep(1)
            if opcao == 1:
                break
            if opcao == 2:
                sleep(1)
                OpcoesDist()
                sleep(2)
            if opcao == 3:
                editar_log()          
                sleep(1)
            if opcao == 0:
                novoLog.write(f"Programa Fechado {data}\n")
                print("\nFechando Programa...")
                sleep(2)
                exit()        
    except(ValueError):
        print("\nValor Inválido\n")
        sleep(1)
    
opcao = 1
while opcao != 0:
    try:
        with open("log.txt", "a") as novoLog:
            opcoes()
            opcao = int(input("\nQual operação gostaria de executar: "))
            if opcao == 1:
                novoLog.write(f"Visualização Acessada {data}\n")
                print(crud.visualizar(listaValores, quantidade))                
                sleep(2)                                    
            elif opcao == 2:
                novoLog.write(f"Alteração Efetuada {data}\n")
                crud.alterar(path, listaValores)                  
                sleep(2)                                    
            if opcao == 3:
                novoLog.write(f"Inclusão Efetuada {data}\n")
                log.append(f"Inclusão Executada {data}")
                crud.incluir(listaValores)
                sleep(2)                                    
            if opcao == 4:
                novoLog.write(f"Exclusão Executada {data}\n")
                crud.excluir(listaValores)
                sleep(2)
            if opcao == 5:
                novoLog.write(f"Relatório Produzido {data}\n")
                print(crud.pruduzirRelatorio(quantidade, "dados.txt"))
                sleep(2)
            if opcao == 0:
                novoLog.write(f"Programa Fechado {data}\n")
                print("\nFechando Programa...")
                sleep(2)
                exit()
            if opcao < 0 or opcao > 5:
                print("Valor inválido")
            with open("dados.txt", "w") as novoEvento:
                    for c, i in enumerate(listaValores):
                        novoEvento.write(f'{i["Dia"]},{i["Quantidade"]}\n')
    except(ValueError):
        print("\nDigite um número válido\n")
        
