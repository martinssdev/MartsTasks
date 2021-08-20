def remove_atividade(lista,numeroDaAtividade):
    """Remove a atividade do dia"""
    lista.pop(int(numeroDaAtividade))

def show_atividades(lista): 
    """Mostra as atividades do dia"""
    for item in lista:
        print(item)


hoje = ['ativ1','ativ2','ativ3']

remove_atividade(hoje,2)
print(hoje)





