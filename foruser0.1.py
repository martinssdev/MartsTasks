# To do List in python by: Martins
# v0.1

domingo = [
    

]

segunda = [
   

]


terça = [

    ]

quarta = [
 
]


quinta = [
 


]


sexta = [


]


sabado = [

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







