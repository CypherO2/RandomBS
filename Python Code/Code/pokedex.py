#pokedex

def Dic(d, k ,v):
    if not k in d:
        d[k] = list()
    d[k].extend(v)
    return d

entries = []
pokenum = []
pokenames = []
Stat_Sheet = []
typegroup = []
gengroup = []
true = ["true","tru","treu","tre","t"]
false = ["f","false","fals","fales","fale","felse"]
Pokedict = {}
choices1 = ["1","2","3","4","5"]
choice2 = ["1","2","3","4","5","6"]

with open("Python Code\Code\pokemon.txt", "r") as file:
    lst = file.readlines()

for el in lst:
    splt_lst = el.strip("\n").split(",")
    entries.append(splt_lst)
    #print(splt_lst)  


pokecount = 0
for el in entries:
    #print(el[1])
    pokenames.append(el[0])
    #print(el[2])
    typegroup.append(el[1])
    #print(el[11])
    gengroup.append(el[10])
    pokecount += 1
    Pokedict = Dic(Pokedict, str(pokecount), el)
#print(Pokedict)

def Menu():
    print("\n+------ Main Menu ------+")
    print("| 1) Search Pokemon     |")
    print("| 2) Search Type        |")
    print("| 3) Search Generation  |")
    print("| 4) Add Pokemon        |")
    print("| 5) Exit               |")
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
            print("\n > > > Poke No., Name, Type 1, Type 2, Total, HP, Atk, Def, Sp.Atk, Sp.Def, Spd, Gen, Legend \n > > >",pokecount,",",entries[P],"\n")
            
def TypeSearch():
    Type = input("\n Please Choose a MAIN Pokemon Typing to Search From \n\n Warning: This Only Works on the MAIN typings of Pokemon Up to and In Generation 6 \n \n > > > ")
    while not Type.capitalize() in typegroup:
        Type = input("\n Please Select a Valid Main Typing \n\n Warning: This Only Works on Pokemon Types Up to and In Generation 6 \n \n > > > ")
    print("\n")
    for el in typegroup:
        Type = Type.capitalize()
        if el in Type:
            T = typegroup.index(el)
            print("\n > > > Poke No., Name, Type 1, Type 2, Total, HP, Atk, Def, Sp.Atk, Sp.Def, Spd, Gen, Legend \n > > >",pokecount,",",entries[T])

def GenSearch():
    Gen = input("\n Please Select a Gen to Choose From \n\n Warning: This only works upto and on Gen 6 \n\n > > > ")
    while not Gen in choice2:
        Gen = input("\n Please Select a Valid Generation! \n\n Warning: This only works upto and on Gen 6 \n\n > > > ")
    for el in gengroup:
        Gen = Gen.capitalize()
        pokecount += 1
        if el in Gen:
            G = gengroup.index(el)
            print("\n > > > Poke No., Name, Type 1, Type 2, Total, HP, Atk, Def, Sp.Atk, Sp.Def, Spd, Gen, Legend \n > > >",pokecount,",",entries[G])

def PokeAdd():
    Name = input("Name of the Pokemon \n > > > ")
    while len(Name) <= 1 or Name.isnumeric():
        Name = input("Please Use An Apporpirate Name \n > > > ")
    Type1 = input("Please Select a Type for the Pokemon \n > > > ")
    while not Type1 in typegroup: 
        Type1 = input("Please Select a Valid Typing \n > > > ")
    Type2 = input("Please Select another Type for the Pokemon \n > > > ")
    while not Type2 in typegroup: 
        Type2 = input("Please Select a Valid Typing \n > > > ")
    hp = input("Please Input a HP \n > > > ")
    while not hp.isnumeric() or not int(hp) > 1 or not int(hp) < 255:
        hp = input("Please Input a Valid HP \n\n Max: 255 \n Min: 1 \n\n > > > ")
    atk = input("Please Input a ATK Value \n > > > ")
    while not atk.isnumeric() or not int(atk) > 1 or not int(atk) < 190:
        atk = input("Please Input a Valid ATK \n\n Max: 190 \n Min: 1 \n\n > > > ")
    Def = input("Please Input a DEF Value \n > > > ")
    while not Def.isnumeric() or not int(Def) > 1 or not int(Def) < 250:
        Def = input("Please Input a Valid DEF \n\n Max: 250 \n Min: 1 \n\n > > > ")
    SpDef = input("Please Input a Sp. DEF Value \n > > > ")
    while not SpDef.isnumeric() or not int(SpDef) > 1 or not int(SpDef) < 230:
        SpDef = input("Please Input a Valid Sp. DEF \n\n Max: 230 \n Min: 1 \n\n > > > ")
    spatk = input("Please Input a Sp. ATK Value \n > > > ")
    while not spatk.isnumeric() or not int(spatk) > 1 or not int(spatk) < 194:
        spatk = input("Please Input a Valid Sp. ATK \n\n Max: 194 \n Min: 1 \n\n > > > ")
    speed = input("Please Input a Speed Value \n > > > ")
    while not speed.isnumeric() or not int(speed) > 5 or not int(speed) < 200:
        speed = input("Please Input a Valid Speed Value \n\n Max: 200 \n Min: 5 \n\n > > > ")
    Gen = input("Please Select a Generation for Your Pokemon \n > > > ")
    while not Gen.isnumeric() or int(Gen) >= 7 or int(Gen) < 1: 
        Gen = input("Please Select a Valid Generation for Your Pokemon \n\n Generations: 1 - 6 | !ONLY! \n\n > > > ")
    Legendary_Status = input("Legendary Status \n\n True or False \n\n > > > ")
    while not Legendary_Status.lower() in true and not Legendary_Status.lower() in false:
         print("\n PLEASE CHOOSE A VALID OPTION: True or False \n")
         Legendary_Status = input("Legendary Status \n\n True or False \n\n > > > ")
    if Legendary_Status.lower() in true:
        Legendary_Status = "True"
    elif Legendary_Status.lower() in false:
        Legendary_Status = "False"
    total = Total(int(hp),int(Def),int(atk),int(SpDef),int(spatk),int(speed))
    Stats = [Name,Type1,Type2,str(total),hp,atk,Def,SpDef,spatk,speed,Gen,Legendary_Status.capitalize()]
    entries.append(Stats)
    print(entries)

def Total(Hp, Def, Atk, SpDef, SpAtk, Spd):
    Total = Hp + Def + Atk + SpDef + SpAtk + Spd
    return Total

x = Menu()
while x in range(1,5):
    if x == 1:
        y = PokeSearch()
        x = Menu()
    elif x == 2:
        y = TypeSearch()
        x = Menu()
    elif x == 3:
        y = GenSearch()
        x = Menu()
    elif x == 4:
        y = PokeAdd()
        x = Menu()
print("\n\n\n < < < Exiting Program > > > ")
exit()