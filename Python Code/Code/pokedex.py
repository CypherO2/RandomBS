#pokedex test 1
entries = []
pokenames = []
choices1 = ["1","2","3"]

with open("Python Code\Code\pokemon.txt", "r") as file:
    lst = file.readlines()

for el in lst:
    splt_lst = el.strip("\n").split(",")
    entries.append(splt_lst)
    #print(splt_lst)  

for el in entries:
    print(el[1])
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
    Pokemon = input("\n Please Select a Pokemon \n \n Warning: This Only Works on Pokemon Up to and In Generation 6 \n \n > > > ")
    while not Pokemon.capitalize() in pokenames:
        Pokemon = input("\n Please Select A Valid Pokemon \n\n Warning: This Only Works on Pokemon Up to and In Generation 6 \n \n > > > ")
    for el in pokenames:
        Pokemon = Pokemon.capitalize()
        if el in Pokemon:
            P = pokenames.index(el)
            print("\n > > > #, Name, Type 1, Type 2, Total, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed, Generation, Legendary \n > > >",entries[P])
            

x = Menu()
while x in range(1,4):
    if x == 1:
        y = PokeSearch()