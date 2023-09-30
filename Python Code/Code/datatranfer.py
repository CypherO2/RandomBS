import sqlite3
from sqlite3 import Error

conn = None
try:
    conn = sqlite3.connect("Python Code\Code\pokemon.db")
    print("Connection Successful\nVersion :", sqlite3.version)
except Error as e:
    print("Connection Failed:", e)

cu = conn.cursor()
print("Cursor Created")

def Data(conn, cu):
    lst1 = []
    temp = """INSERT INTO Pokemon(Name, Type1, Type2, Total, HP, ATK, DEF, SPDEF, SPATK, Speed, Generation, Legendary_Status) Values(?,?,?,?,?,?,?,?,?,?,?,?)"""
    with open("Python Code\Code\pokemon.txt", "r") as file:
        lst = file.readlines()
    for el in lst:
        splt_lst = el.strip("\n").split(",")
        lst1.append(splt_lst)
        # print(splt_lst)
    count = 0
    for el in lst1:
        record = (
            (el[0]),
            (el[1]),
            (el[2]),
            (el[3]),
            (el[4]),
            (el[5]),
            (el[6]),
            (el[7]),
            (el[8]),
            (el[9]),
            (el[10]),
            (el[11]),
        )
        count = count + 1
        try:
            cu.execute(temp, record)
            conn.commit()
            print("Successfully Added", count)
        except Error as e:
            print("An Error Occured:", e, "\n Project Not Committed")


Data(conn, cu)


conn.close()
print("Connection Closed")
