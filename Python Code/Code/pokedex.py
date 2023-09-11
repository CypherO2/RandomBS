#pokedex test 1
entries = []
pokenames = []
typegroup = []
choices1 = ["1","2","3"]

with open("Python Code\Code\pokemon.txt", "r") as file:
    lst = file.readlines()

for el in lst:
    splt_lst = el.strip("\n").split(",")
    entries.append(splt_lst)
    #print(splt_lst)  

for el in entries:
#    print(el[1])
    pokenames.append(el[1])

for el in entries:
    print(el[2])
    typegroup.append(el[2])

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
            print("\n > > > Poke No., Name, Type 1, Type 2, Total, HP, Atk, Def, Sp.Atk, Sp.Def, Spd, Gen, Legend \n > > >",entries[P],"\n")
            
def TypeSearch():
    Type = input("\n Please Choose a MAIN Pokemon Typing to Search From \n\n Warning: This Only Works on the MAIN typings of Pokemon Up to and In Generation 6 \n \n > > > ")
    while not Type.capitalize() in typegroup:
        Type = input("\n Please Select a Valid Main Typing \n\n Warning: This Only Works on Pokemon Types Up to and In Generation 6 \n \n > > > ")
    print("\n")
    for el in typegroup:
        Type = Type.capitalize()
        if el in Type:
            T = typegroup.index(el)
            print("\n > > > Poke No., Name, Type 1, Type 2, Total, HP, Atk, Def, Sp.Atk, Sp.Def, Spd, Gen, Legend \n > > >",entries[T])

x = Menu()
while x in range(1,4):
    if x == 1:
        y = PokeSearch()
        x = Menu()
    elif x == 2:
        y = TypeSearch()
        