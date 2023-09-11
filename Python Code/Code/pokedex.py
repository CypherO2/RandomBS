#pokedex test 1
entries = []
choices1 = ["1","2","3","4"]

file = open("Python Code\Code\pokemon.txt","r")
for el in file:
    entry = el.split("\n")
    entries.append(entry)

def Menu():
    print("+------ Main Menu ------+")
    print("| 1) Search Pokemon     |")
    print("| 2) Search Type        |")
    print("| 3) Search Generation  |")
    print("+-----------------------+")
    choice = input("Please Select One of the Above \n > > > ")
    while not choice in choices1: 
        choice = input("Please ONLY Select One of the Above \n > > > ")
    return int(choice)

