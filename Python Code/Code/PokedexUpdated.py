import sqlite3
from sqlite3 import Error
import pandas as pd
from PokeFunc import *

# Establishes A Connection to the Database
conn = None
try:
    conn = sqlite3.connect("Python Code/Code/pokemon.db")
    print("Connection Successful\nVersion :", sqlite3.version)
except Error as e:
    print("Connection Failed:", e)

# Create A Cursor
cu = conn.cursor()
print("Cursor Created")

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
