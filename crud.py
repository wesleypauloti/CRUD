from time import sleep
import mtc
import MedidasVar
import Distribuicao

def visualizar(listaValores, dados):
    print()
    for c, i in enumerate(listaValores):
        print(f'{c + 1} - {i["Dia"]} tivemos um total de {i["Quantidade"]} Registros')
        
    print(f'\n{mtc.media(dados)} registros durante a semana')
    print(f'Moda: {mtc.moda(dados)}')
    print(f'{mtc.mediana(dados)} registros durante a semana')
    print(f'Valor da Variância: {MedidasVar.variancia(dados):.2f} registros por semana')
    print(f'Valor do Desvio Padrão: {MedidasVar.desvioPadrao(dados):.2f} registros por semana\n')
    return

def alterar(path, listaValores):
    print()
    for c, i in enumerate(listaValores):
        print(f'{c + 1} - {i["Dia"]} tivemos um total de {i["Quantidade"]} Registros')
    valorAlterado = False
    while not valorAlterado:
        try:
            dia = input("\nGostaria de alterar o valor de qual dia da Semana[Ex:Segunda]: ").title()
            for c, i in enumerate(listaValores):
                if i["Dia"] == dia:
                    novoValor = int(input("\nQual valor gostaria de inserir: "))
                    i["Quantidade"] = novoValor                          
                    print("Valor alterado com sucesso\n")
                    valorAlterado = True
                    break
                else:
                    if c == len(listaValores) - 1:
                        print("\nDia digitado não encontrado")
        except(ValueError):
            print("Valor incorreto")  
    return listaValores
        
def incluir(listaValores):
    print()
    for c, i in enumerate(listaValores):
        print(f'{c + 1} - {i["Dia"]} tivemos um total de {i["Quantidade"]} Registros')
    while True:
        try:
            linha = int(input("\nEm qual linha gostaria de inserir um novo Registro: "))
            if linha > 0 and linha <= len(listaValores) + 1:
                evento = input("Qual nome do evento[Ex:Feriado]: ").title()
                conteudo = input("Qual conteúdo gostaria de inserir: ")
                novoItem = {"Dia": evento, "Quantidade": conteudo}
                listaValores.insert(linha - 1, novoItem)
                print("Incluido com Sucesso!\n")
                break
            else:
                print("\nValor inválido\n")
                sleep(1)
        except(ValueError):
            print("\nValor inválido\n")
            sleep(1)
    return listaValores

def excluir(listaValores):
    print()
    for c, i in enumerate(listaValores):
        print(f'{c + 1} - {i["Dia"]} tivemos um total de {i["Quantidade"]} Registros')
    while True:
        try:
            linha = int(input("\nQual linha gostaria de Excluir: "))
            if linha > 0 and linha <= len(listaValores): 
                listaValores.pop(linha - 1)
                print("Excluido com Sucesso!\n")
                break
            else:
                print("\nValor inválido\n")
                sleep(1)
        except(ValueError):
            print("\nValor inválido\n")
            sleep(1)
    return listaValores


def pruduzirRelatorio(dados, path):
    # Gerando um relatório
    with open("relatorio.txt", "w") as arquivo2:
        arquivo2.write(f'Relatório do arquivo {path}'
                    f'\n\nMEDIDADES E TENDÊNCIA CENTRAL'
                    f'\n\n{mtc.media(dados)} registros durante a semana'
                    f'\nModa: {mtc.moda(dados)}'
                    f'\n{mtc.mediana(dados)} registros durante a semana'
                    f'\n\nDESVIOS'
                    f'\n\nValor da Variância: {MedidasVar.variancia(dados):.2f} registros por semana'
                    f'\nValor do Desvio Padrão: {MedidasVar.desvioPadrao(dados):.2f} registros por semana\n'
                    
    f'\n\nProgramador resposável: Wesley Paulo')        

    return '\nFoi gerado um relatório\n'