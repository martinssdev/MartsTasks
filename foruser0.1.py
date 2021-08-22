# To do List in python by: Martins
# v0.1

import functions as f

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








