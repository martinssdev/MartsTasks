# To do List in python by: Martins
# v0.1

import functions as f





def main():
    f.greet_user()
    
    day = input("Hello! Welcome, today is ? \n")
    
    with open(f'{day}.txt','r') as fobj:
            f.show_activities(day) # NÃO SEI TB SE PRECISO DEIXAR ESSE WHILE DENTRO DO OPEN FILE, ACREDITO Q N
            keyword = 't' # resolver isso dps 
            while f.check_event(keyword):
               keyword = input("Digite 'q' para sair do programa\n")
    
        
            

if __name__ == "__main__":
   main()









