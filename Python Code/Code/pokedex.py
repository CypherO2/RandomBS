#pokedex test 1
entries = []

file = open("Assets\pokemon.txt","r")
for el in file:
    entry = el.split("\n")
    print(entry)

#def PokeSearch():
