
def remove_activities(day,activity):
    """Remove one actvity"""
    with open(f'{day}.txt','r') as fobj:
        activities = fobj.readlines()

        # FIX THIS!


    activities.pop(int(activity))

def show_activities(day): 
    """Show the activities of the day"""
    
    
    with open(f'{day}.txt','r') as fobj:
        activities = fobj.readlines()

        for activity in activities:
    
            print(str(activities.index(activity)) + " -> " + activity)


def list_activities(lista):
    """Lists all the acticvities"""
    pass


def create_file_user():
    """Create the archive with user info"""
    UserInfos = 'userinfo.txt'
    with open(UserInfos,'w') as file_object:
        name = input("Write your name\n")
        username = input("Write your nickname\n")
        age = input("Write your age\n")
        file_object.write(("Infos do user:\n"))
        file_object.write("Name:"+ name + "\n")
        file_object.write("Username:" + username + "\n")
        file_object.write("Age:" + age + "\n")


def greet_user():
    userInfos = 'userinfo.txt'

    try:
        with open(userInfos,'r') as fobj:
            
            fobj.readlines()
            
                
    except FileNotFoundError:
            create_file_user()
            add_activities()
            greet_user()
            
    else:
        with open(userInfos,'r') as fobj:
            lines = fobj.readlines()
            for line in lines:
                print(line)
            


def add_activities():
    """Add the Activities in the first use"""
    days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']


    for day in days:
        enter = ''
        day = f'{day}.txt'
        with open(day,'w') as fobj:
            while enter != 'q':
                enter = input(f"Write the activities of {day} 'q' to write for the next day\n")
                fobj.write(enter + "\n")

 
    




