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

    '4hrs Igd',
    '20min Leitura - Livro da Economia',
    '20 min Guia Suno '
    '1Unidade espanhol',
    '30min Iezzi',
    '1partida lol',
    '3partidas xadrez blitz',
    '2hrs python'

]


terça = [
    'Violino 30min',
    'IVC 4Hrs',
    '3partidas de xadrez blitz',
    '1partida de lol',
    '1unidade inglês',
    '2hrs Devweb',
    '20min livro da economia',
    '20min guia suno'
    
    ]

quarta = [
    
    '4Hrs IGD',
    '1unidade Espanhol',
    '1partida de lol',
    '3partidas blitz',
    '20min - Livro da economia',
    '2hrs Linux',
    '20min Guia Suno ações'

]


quinta = [

    '4hrs IVC',
    '1unidade inglês',
    '20min Leitura - Código Limpo',
    '30min guidorizzi',
    '1partida de Lol',
    '3partidas blitz xadrez',


]


sexta = [

    '4hrs igd',
    '1unidade espanhol',
    '1partida de Lol',
    '3partidas xadrez blitz',
    '2hrs Python',
    '20min livro da economia',
    '20min guia suno ações'
]


sabado = [

    '1unidade inglês',
    '20min Leitura- Livro da Economia',
    '30min Xadrez',
    '1partida de LOl',
    '3partidas xadrez blitz',
    '4hrs IVC',
    '2hrs devWeb',
    '20min guia suno ações'

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







