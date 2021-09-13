# To do List in python by: Martins
# v0.1

import functions as f





def main():
    f.greet_user()
    
    day = input("Hello! Welcome, today is ? \n")
    
    with open(f'{day}.txt','r') as fobj:
            f.show_activities(day)
        
    
        
            

if __name__ == "__main__":
   main()









