# To do List in python by: Martins
# v0.1

# IDEIAS: 
# USER_PROFILE()
# TEMPO DE USO ATÉ CONCLUIR AS ATIVIDADES COM IMPORT TIME
import functions as f


domingo = [

    'IVC 4Hrs',
    'Inglês 1 unidade',
    '20min Leitura - Livro da Economia',
    '30min Halliday',
    '1partida de lol',
    '3partidas xadrez blitz',
    '2hrs linux',
    '20min guia suno'



]

segunda = [

    '0-4hrs Igd',
    '1-20min Leitura - Caos James Gleick',
    '2-1Unidade espanhol',
    '3-30min Iezzi',
    '4-1partida lol',
    '5-3partidas xadrez blitz',
    '6-2hrs python'

]


terça = [
    '0-Violino 30min',
    '2-IVC 4Hrs',
    '3-3partidas de xadrez blitz',
    '4-1partida de lol',
    '5-1unidade inglês',
    '6-2hrs Devweb',
    '7-20min livro da economia',
    '8-20min guia suno'
    
    ]

quarta = [
    
    '0-4Hrs IGD',
    '1-1unidade Espanhol',
    '2-1partida de lol',
    '3-3partidas blitz',
    '4-20min - Livro da economia',
    '5-2hrs Linux',
    '6-20min Guia Suno ações'

]


quinta = [

    '0-4hrs IVC',
    '1-1unidade inglês',
    '2-20min Leitura - Código Limpo',
    '3-30min guidorizzi',
    '4-1partida de Lol',
    '5-3partidas blitz xadrez',


]


sexta = [

    '0-4hrs igd',
    '1-1unidade espanhol',
    '2-1partida de Lol',
    '3-3partidas xadrez blitz',
    '4-2hrs Python',
    '5-20min livro da economia',
    '6-20min guia suno ações'
]


sabado = [

    '0- 1unidade inglês',
    '1- 20min Leitura- Livro da Economia',
    '2-30min Xadrez',
    '3-1partida de LOl',
    '4-3partidas xadrez blitz',
    '5- 4hrs IVC',
    '6-2hrs devWeb',
    '7-20min guia suno ações'

]







class Dia():
    """Classe para o Dia da semana"""
    def __init__(self,nome):
        """Inicialização do dia"""
        self.nome = nome
        




program_active = True


dia = input("Bem vindo ao tasks (by: Marts)\nQue dia é hoje?\n")


while program_active == True:

    if dia == 'domingo':
        
        print(dia.title() + ":")
        f.show_atividades(domingo)

        atividadeConcluida = input("Alguma atividade concluida?\n")
        if atividadeConcluida == 's':

            numeroDaAtividade = input("Qual atividade?\n")
            f.remove_atividade(domingo,numeroDaAtividade)
               

    if dia == 'segunda':

        print(dia.title() + ":")
        f.show_atividades(segunda)

        atividadeConcluida = input("Alguma atividade concluida?\n")
        if atividadeConcluida == 's':

            numeroDaAtividade = input("Qual atividade?\n")
            f.remove_atividade(segunda,numeroDaAtividade)


    if dia == 'terça':

        print(dia.title() + ":")
        f.show_atividades(terça)

        atividadeConcluida = input("Alguma atividade concluida?\n")
        if atividadeConcluida == 's':

            numeroDaAtividade = input("Qual atividade?\n")
            f.remove_atividade(terça,numeroDaAtividade)
              
          

    if dia == 'quarta':
        
        print(dia.title() + ':')
        f.show_atividades(quarta)
        
        atividadeConcluida = input("Alguma atividade concluida?\n")
        if atividadeConcluida == 's':

            numeroDaAtividade = input("Qual atividade?\n")
            f.remove_atividade(quarta,numeroDaAtividade)
            




    if dia == 'quinta':

        print(dia.title() + ':')
        f.show_atividades(quinta)
        
        atividadeConcluida = input("Alguma atividade concluida?\n")
        if atividadeConcluida == 's':

            numeroDaAtividade = input("Qual atividade?\n")
            f.remove_atividade(quinta,numeroDaAtividade)
            


            



    if dia == 'sexta':
        print(dia.title() + '')
        f.show_atividades(sexta)

        atividadeConcluida = input("Alguma atividade concluida?\n")
        if atividadeConcluida == 's':

            numeroDaAtividade = input("Qual atividade?\n")
            f.remove_atividade(sexta,numeroDaAtividade)




    if dia == 'sabado':

        print(dia.title() + ':')
        f.show_atividades(sabado)

        atividadeConcluida = input("Alguma atividade concluida?\n")
        if atividadeConcluida == 's':

            numeroDaAtividade = input("Qual atividade?\n")
            f.remove_atividade(sabado,numeroDaAtividade)
               




    continuarUsando  =  input("Deseja continuar usando o MartinsTasks?\n")
    
    if continuarUsando == 'n':
        program_active = False







