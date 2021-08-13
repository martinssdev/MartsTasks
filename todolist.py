# To do List in python by: Martins
# v0.1

domingo = [
    '0-IVC 4Hrs',
    '1-Inglês 1 unidade',
    '2-20min Leitura - Livro da Economia',
    '3-30min Halliday',
    '4-1partida de lol',
    '5-3partidas xadrez blitz'



]

segunda = [
    '0-4hrs Dinâmica não Linear',
    '1-20min Leitura - Caos James Gleick',
    '2-1Unidade espanhol',
    '3-30min Iezzi',
    '4-1partida lol',
    '5-3partidas xadrez blitz'

]


terça = [
    '0-Violino 30min',
    '1-Great Gatsby 20min',
    '2-IVC 4Hrs',
    '3-3partidas de xadrez blitz',
    '4-1partida de lol',
    '5-1unidade inglês']

quarta = [
    '0-4Hrs ivc',
    '1-1unidade Espanhol',
    '2-1partida de lol',
    '3-3partidas blitz'


]


quinta = [
    '0-4hrs Igd',
    '1-1unidade inglês',
    '2-20min Leitura - Código Limpo',
    '3-30min guidorizzi',
    '4-1partida de Lol',
    '5-3partidas blitz xadrez'



]


sexta = [
    '0-4hrs Igd',
    '1-20min Leitura - Bíblia do Linux',
    '2-1unidade espanhol',
    '3-30min Python',
    '4-1partida de Lol',
    '5-3partidas xadrez blitz'

]


sabado = [
    '0-4Hrs Dinâmica não linear',
    '1- 1unidade inglês',
    '2- 20min Leitura- Livro da Economia',
    '3-30min Xadrez',
    '4-1partida de LOl',
    '5-3partidas xadrez blitz'

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







