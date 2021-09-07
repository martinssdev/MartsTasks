
def remove_atividade(lista,numeroDaAtividade):
    """Remove a atividade do dia"""
    lista.pop(int(numeroDaAtividade))

def show_atividades(lista): 
    """Mostra as atividades do dia"""

    for item in lista:
    
            print(str(lista.index(item)) + " " + item)


def listar_atividades(lista):
    """Listar todas as atividades"""
    pass


def criar_arquivo():
    """Criar o arquivo que contém as informações do usuário"""
    arquivoAtividades = 'arquivoAtividades.txt'
    with open(arquivoAtividades,'w') as file_object:
        nome = input("Digite seu Nome\n")
        nickname = input("Digite seu nickname\n")
        idade = input("Digite sua idade\n")
        file_object("Infos do user:\n")
        file_object.write("Nome:"+ nome + "\n")
        file_object.write("User:" + nickname + "\n")
        file_object.write("Idade:" + idade + "\n")


def adicionar_atividades():
    """Adiciona as atividades da semana no primeiro uso"""
    arquivoAtividades = 'arquivoAtividades.txt'
    with open(arquivoAtividades,'a') as file_object:
        pass
    
    pass
    
    




