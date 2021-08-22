
def remove_atividade(lista,numeroDaAtividade):
    """Remove a atividade do dia"""
    lista.pop(int(numeroDaAtividade))

def show_atividades(lista): 
    """Mostra as atividades do dia"""

    for item in lista:
    
            print(str(lista.index(item)) + " " + item)

        
hoje = ['ativ1','ativ2']




