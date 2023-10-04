import sqlite3
from sqlite3 import Error
import pandas as pd

# Used Letters: x


# Main Menu Function - Displays Options - Allows for Fluid Use of Program
def Menu():
    print("\n+------ Main Menu ------+")
    print("| 1) Search Pokemon     |")
    print("| 2) Search Type        |")
    print("| 3) Search Generation  |")
    print("| 4) Add Pokemon        |")
    print("| 5) Exit               |")
    print("+-----------------------+")
    c = input("Please Select One of the Above \n > > > ")
    while not c.isnumeric() and not int(c) in range(1, 6):
        choice = input("Please ONLY Select One of the Above \n > > > ")
    return int(c)

# Allows User to Search Database for Any Pokemon Within It
def SearchPokemon(conn, cu):
    q = """SELECT * From Pokemon WHERE Name = ?"""
    inp = input("Select a Pokemon\n\n!Gen 1 - 6 Only!\n\n > > > ")
    inp = inp.lower().capitalize()
    check = PokemonNameCheck(conn, cu, inp)
    while not inp:
        inp = input("Select a Pokemon\n\n!Gen 1 - 6 Only!\n\n > > > ")
        inp = inp.lower().capitalize()
        check = PokemonNameCheck(conn, cu, inp)
    cu.execute(q, (inp,))
    result = cu.fetchall()
    df = pd.DataFrame(result)
    df.columns = ["ID","Name","Type1","Type2","Total","HP","ATK","DEF","SP DEF","SP ATK","Spd","Gen","Legend?"]
    print(df)


# Checks The Name Against the Database to Prevent Crashes (Input Validation)
def PokemonNameCheck(conn, cu, val):
    q = """SELECT Name FROM Pokemon"""
    cu.execute(q)
    result = cu.fetchall()
    for i in result:
        if i[0] == val:
            print("Pokemon Found")
            return True
    print("Pokemon Not Found!")
    return False


# Search Pokemon Based On Types IN Database
def SearchType(conn, cu):
    q = """Select * FROM Pokemon WHERE Type1 OR Type2 = ?"""
    inp = input("Select a Type\n\nEither Type 1 or 2! \n NOT BOTH!\n > > > ")
    inp = inp.lower().capitalize()
    check = PokemonTypeCheck(conn, cu, inp)
    while not check:
        inp = input("Select a Type\n\nEither Type 1 or 2! \n NOT BOTH!\n > > > ")
        inp = inp.lower().capitalize()
        check = PokemonTypeCheck(conn, cu, inp)
    cu.execute(q, (inp,))
    result = cu.fetchall()
    df = pd.DataFrame(result)
    df.columns = ["ID","Name","Type1","Type2","Total","HP","ATK","DEF","SP DEF","SP ATK","Spd","Gen","Legend?"]
    print(df)


# Pokemon Type Checker (Input Validation)
def PokemonTypeCheck(conn, cu, val):
    q = """SELECT Type1, Type2 FROM Pokemon"""
    cu.execute(q)
    result = cu.fetchall()
    for i in result:
        if i[0] == val:
            print("Type Found")
            return True
    print("Type NOT Found")
    return False


# Search Based on Pokemon Generations - UP TO 6th (For Now?)
def SearchGen(conn, cu):
    q = """SELECT * FROM Pokemon WHERE Generation = ?"""
    inp = input("Pokemon Generation\n\nUp To The 6th Generation\n\n > > > ")
    check = PokemonGenCheck(conn, cu, inp)
    while not check or not inp.isnumeric():
        inp = input("Pokemon Generation\n\nUp To The 6th Generation\n\n > > > ")
        check = PokemonGenCheck(conn, cu, inp)
    cu.execute(q, (int(inp),))
    result = cu.fetchall()
    df = pd.DataFrame(result)
    df.columns = ["ID","Name","Type1","Type2","Total","HP","ATK","DEF","SP DEF","SP ATK","Spd","Gen","Legend?"]
    print(df)


# Pokemon Generation Checker (Input Validation)
def PokemonGenCheck(conn, cu, val):
    q = """SELECT Generation FROM Pokemon"""
    cu.execute(q)
    result = cu.fetchall()
    for i in result:
        if i[0] == int(val):
            print("Generation Found!")
            return True
    print("Generation NOT Found!")
    return False

# Function to Add Value together
def Total(Hp, Def, Atk, SpDef, SpAtk, Spd):
    Total = Hp + Def + Atk + SpDef + SpAtk + Spd
    return Total

# Function to Add Pokemon to Database
def AddPokemon(conn,cu):
    value = """INSERT INTO Pokemon(Name, Type1, Type2, Total, HP, ATK, DEF, SPDEF, SPATK, Speed, Generation, Legendary_Status) Values(?,?,?,?,?,?,?,?,?,?,?,?)"""
    Name = input("Pokemon Name\n > > > ")
    check = PokemonNameCheck(conn,cu,Name)
    while check:
        Name = input("Pokemon Name\n > > > ")
        check = PokemonNameCheck(conn,cu,Name)
    Type1 = input("Pokemon Primary Type\n > > > ")
    check = PokemonTypeCheck(conn,cu,Type1)
    while not check:
        Type1 = input("Input Valid Primary Type\n > > > ")
        check = PokemonTypeCheck(conn,cu,Type2)
    Type2 = input("Pokemon Secondary Type\n\nThis CAN be left blank.\n\n > > > ")
    check = PokemonTypeCheck(conn,cu,Type2)
    print(Type2)
    while not check and not Type2 == "":
        Type2 = input("Input Valid Secondary Type\n > > > ")
        check = PokemonTypeCheck(conn,cu,Type2)
    HP = input("Please Input a HP \n > > > ")
    while not HP.isnumeric() or not int(HP) in range(1,256):
        HP = input("Please Input a Valid HP \n\n Max: 255 \n Min: 1 \n\n > > > ")
    ATK = input("Please Input a ATK Value \n > > > ")
    while not ATK.isnumeric() or not int(ATK) in range(1,191):
        ATK = input("Please Input a Valid ATK \n\n Max: 190 \n Min: 1 \n\n > > > ")
    DEF = input("Please Input a DEF Value \n > > > ")
    while not DEF.isnumeric() or not int(DEF) in range(1,251):
        DEF = input("Please Input a Valid DEF \n\n Max: 250 \n Min: 1 \n\n > > > ")
    SPDEF = input("Please Input a Sp. DEF Value \n > > > ")
    while not SPDEF.isnumeric() or not int(SPDEF) in range(1,231):
        SPDEF = input("Please Input a Valid Sp. DEF \n\n Max: 230 \n Min: 1 \n\n > > > ")
    SPATK = input("Please Input a Sp. ATK Value \n > > > ")
    while not SPATK.isnumeric() or not int(SPATK) in range(195):
        SPATK = input("Please Input a Valid Sp. ATK \n\n Max: 194 \n Min: 1 \n\n > > > ")
    SPD = input("Please Input a Speed Value \n > > > ")
    while not SPD.isnumeric() or not int(SPD) in range(5,201):
        SPD = input("Please Input a Valid Speed Value \n\n Max: 200 \n Min: 5 \n\n > > > ")
    Gen = input("Please Select a Generation for Your Pokemon \n > > > ")
    while not Gen.isnumeric() or not int(Gen) in range(1,7): 
        Gen = input("Please Select a Valid Generation for Your Pokemon \n\n Generations: 1 - 6 | !ONLY! \n\n > > > ")
    Legendary_Status = input("Legendary Status \n\n True or False \n\n > > > ")
    while not Legendary_Status.lower().capitalize() in true and not Legendary_Status.lower().capitalize() in false:
         print("\n PLEASE CHOOSE A VALID OPTION: True or False \n")
         Legendary_Status = input("Legendary Status \n\n True or False \n\n > > > ")
    if Legendary_Status.lower().capitalize() in true:
        Legendary_Status = "True"
    elif Legendary_Status.lower().capitalize() in false:
        Legendary_Status = "False"
    total = Total(int(HP),int(DEF),int(ATK),int(SPDEF),int(SPATK),int(SPD))
    record = (Name,Type1,Type2,total,HP,DEF,ATK,SPDEF,SPATK,SPD,Gen,Legendary_Status)
    try:
        cu.execute(value, record)
        conn.commit()
        print("Successfully Added")
    except Error as e:
        print("An Error Occured:", e, "\n Project Not Committed")

# Establishes A Connection to the Database
conn = None
try:
    conn = sqlite3.connect("Code\pokemon.db")
    print("Connection Successful\nVersion :", sqlite3.version)
except Error as e:
    print("Connection Failed:", e)

# Create A Cursor
cu = conn.cursor()
print("Cursor Created")

# True/False List of Accepted Responses
true = ["True","Tru","Treu","Tre","T"]
false = ["F","False","Fals","Fales","Fale","Felse"]

# Calls Menu
x = Menu()
while x in range(1, 5):
    # Allows User to Search For Any Pokemon Within the Database
    if x == 1:
        SearchPokemon(conn, cu)
        print("\n")
        x = Menu()
    # Allows User to Search For Any Pokemon Type Within the Database
    elif x == 2:
        SearchType(conn, cu)
        print("\n")
        x = Menu()
    # Allows User to Search For Any Pokemon's Generation Within the Database
    elif x == 3:
        SearchGen(conn, cu)
        print("\n")
        x = Menu()
    # Allows User to Add Pokemon to the Database
    elif x == 4:
        AddPokemon(conn,cu)
        print("\n")
        x = Menu()

# Closes Connection to Database
conn.close()
print("Connection Closed")
