#pokedex test 1
entries = []
pokenames = []
choices1 = ["1","2","3","4","5"]

with open("Python Code\Code\pokemon.txt", "r") as file:
    lst = file.readlines()

for el in lst:
    splt_lst = el.strip("\n").split(",")
    entries.append(splt_lst)
    #print(splt_lst)  

for el in entries:
    #print(el[1])
    pokenames.append(el[1])

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

def PokeSearch():
    Pokemon = input("\n Please Select a Pokemon \n > > > ")


