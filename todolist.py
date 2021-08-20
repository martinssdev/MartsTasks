# To do List in python by: Martins
# v0.1

# IDEIAS: 
# USER_PROFILE()
# TEMPO DE USO ATÉ CONCLUIR AS ATIVIDADES COM IMPORT TIME


domingo = [

    '0-IVC 4Hrs',
    '1-Inglês 1 unidade',
    '2-20min Leitura - Livro da Economia',
    '3-30min Halliday',
    '4-1partida de lol',
    '5-3partidas xadrez blitz',
    '6-2hrs linux',
    '7-20min guia suno'



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


program_active = True


dia = input("Bem vindo ao tasks (by: Marts)\nQue dia é hoje?\n")


while program_active == True:

    if dia == 'domingo':
        
        print('Domingo:\n')
        for item in domingo:
            print(item)

        bl2 = input("Alguma atividade concluida?\n")
        if bl2 == 's':

            numeroDaAtividade = input("Qual atividade?\n")
            domingo.pop(int(numeroDaAtividade))
               

    if dia == 'segunda':

        print("Segunda feira\n")
        for item in segunda:
            print(item)

        bl2 = input("Alguma atividade concluida?\n")
        if bl2 == 's':

            numeroDaAtividade = input("Qual atividade?\n")
            segunda.pop(int(numeroDaAtividade))
            


    if dia == 'terça':

        print("Terça:\n")
        for item in terça:
            print(item)

        bl2 = input("Alguma atividade concluida?\n")
        if bl2 == 's':

            numeroDaAtividade = input("Qual atividade?\n")
            terça.pop(int(numeroDaAtividade))
              
          

    if dia == 'quarta':
        
        print('Quarta:\n')
        for item in quarta:
            print(item)
        
        bl2 = input("Alguma atividade concluida?\n")
        if bl2 == 's':

            numeroDaAtividade = input("Qual atividade?\n")
            quarta.pop(int(numeroDaAtividade))
            




    if dia == 'quinta':

        print('Quinta:\n')
        for item in quinta:
            print(item)
        
        bl2 = input("Alguma atividade concluida?\n")
        if bl2 == 's':

            numeroDaAtividade = input("Qual atividade?\n")
            quinta.pop(int(numeroDaAtividade))
            


            



    if dia == 'sexta':
        print('Sexta:\n')
        for item in sexta:
            print(item)

        bl2 = input("Alguma atividade concluida?\n")
        if bl2 == 's':

            numeroDaAtividade = input("Qual atividade?\n")
            sexta.pop(int(numeroDaAtividade))




    if dia == 'sabado':

        print('Sábado:\n')
        for item in sabado:
            print(item)

        bl2 = input("Alguma atividade concluida?\n")
        if bl2 == 's':

            numeroDaAtividade = input("Qual atividade?\n")
            sabado.pop(int(numeroDaAtividade))
               




    bl1  =  input("Deseja continuar usando o MartinsTasks?\n")
    
    if bl1 == 'n':
        program_active = False







