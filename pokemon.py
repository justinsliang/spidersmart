import random

print("Welcome to Pokemon")

p1deck = []
p2deck = []

class Attack:
    def __init__(self, name, damage, critChance, uses):
        self.name = name
        self.damage = damage
        self.critChance = critChance
        self.uses = uses

class Card:
    def __init__(self, name, type, health, attacks):
        self.name = name
        self.type = type
        self.health = health
        self.attacks = attacks

#LIST OF POKEMON TO CHOOSE FROM
POKEMONLIST =  [Card("Pikachu",     "ELECTRIC", 100,   [Attack("Quick Attack", 10, 1, 100), 
                                                        Attack("Thunderbolt", 25, 4, 4), 
                                                        Attack("Electro Ball", 40, 0.5, 2)]),
                Card("Bulbasaur",   "GRASS",    100,   [Attack("Quick Attack", 10, 1, 100), 
                                                        Attack("Vine Whip", 25, 4, 4), 
                                                        Attack("Razor Leaf", 40, 0.5, 2)]),
                Card("Squirtle",    "WATER",    100,   [Attack("Quick Attack", 10, 1, 100), 
                                                        Attack("Water Gun", 25, 4, 4), 
                                                        Attack("Hydro Pump", 40, 0.5, 2)]),
                Card("Beedrill",    "GRASS",    70,    [Attack("Quick Attack", 15, 1, 100), 
                                                        Attack("Bug Bite", 30, 4, 4), 
                                                        Attack("Drill Sting", 45, 0.5, 2)]),
                Card("Electabuzz",  "ELECTRIC", 200,   [Attack("Quick Attack", 10, 1, 100), 
                                                        Attack("Hyper ", 20, 4, 2), 
                                                        Attack("Hydro Pump", 40, 0.5, 1)]),
                Card("Poliwrath",   "WATER",    150,   [Attack("Quick Attack", 10, 1, 100), 
                                                        Attack("Belly Drum", 20, 4, 2), 
                                                        Attack("Rain Dance", 40, 0.5, 1)]),
                Card("Rillaboom",   "GRASS",    300,   [Attack("Quick Attack", 20, 1, 100), 
                                                        Attack("Bug Bite", 40, 4, 2), 
                                                        Attack("Drill Sting", 80, 0.5, 1)]),
                Card("Zekrom",      "ELECTRIC", 300,   [Attack("Quick Attack", 20, 1, 100), 
                                                        Attack("Ancient Power", 40, 4, 2), 
                                                        Attack("Thunder Fang", 80, 0.5, 1)]),
                Card("Poliwrath",   "WATER",    150,   [Attack("Quick Attack", 10, 1, 100), 
                                                        Attack("Belly Drum", 20, 4, 2), 
                                                        Attack("Rain Dance", 40, 0.5, 1)])]

def isWin():
    output = 0
    p1dead = 0
    p2dead = 0
    for i in range(0, 3):
        if p1deck[i].health == 0:
            p1dead += 1
        if p2deck[i].health == 0:
            p2dead += 1
    if p1dead == 3:
        output = 1
    if p2dead == 3:
        output = 2
    if p1dead == 3 and p2dead == 3:
        output = 3
    return output

def getDamage(dindex: int, ddeck: list, aindex: int, adeck: list, attack: int):
    adeck[aindex].attacks[attack].uses -= 1

    #placeholder return
    typeMultiplier = 1
    if adeck[aindex].type == "ELECTRIC" and ddeck[dindex].type == "GRASS":
        typeMultiplier = 1.5
    if adeck[aindex].type == "GRASS" and ddeck[dindex].type == "WATER":
        typeMultiplier = 1.5
    if adeck[aindex].type == "WATER" and ddeck[dindex].type == "ELECTRIC":
        typeMultiplier = 1.5


    
    doCrit = random.randint(0, 9)
    if doCrit <= adeck[aindex].attacks[attack].critChance:
        doCrit = 2
    else: 
        doCrit = 1

    damage = typeMultiplier * (adeck[aindex].attacks[attack].damage) * doCrit
    ddeck[dindex].health -= damage
    if ddeck[dindex].health < 0:
        ddeck[dindex].health = 0
    return damage

print("List of Pokemon:")
for i in range(0, len(POKEMONLIST)):
    print(f"{i} - Name: {POKEMONLIST[i].name}, Type: {POKEMONLIST[i].type}, Health: {POKEMONLIST[i].health}")

for i in range(0, 3):
    choice = int(input(f"Player 1, choose your pokemon ({i}): "))
    p1deck.append(POKEMONLIST[choice])

print("List of Pokemon:")
for i in range(0, len(POKEMONLIST)):
    print(f"{i} - Name: {POKEMONLIST[i].name}, Type: {POKEMONLIST[i].type}, Health: {POKEMONLIST[i].health}")

for i in range(0, 3):
    choice = int(input(f"Player 2, choose your pokemon ({i}): "))
    p2deck.append(POKEMONLIST[choice])

for i in range(0, 3):
    print(f"{i}: {p1deck[i].name}")
p1index = int(input("P1 choose your pokemon: "))

for i in range(0, 3):
    print(f"{i}: {p2deck[i].name}")
p2index = int(input("P2 choose your pokemon: "))
turn = 1

option = ""
while isWin() == 0:
    print(f"Player 1 - Name: {p1deck[p1index].name}, Type: {p1deck[p1index].type}, Health: {p1deck[p1index].health}")
    print(f"Player 2 - Name: {p2deck[p2index].name}, Type: {p2deck[p2index].type}, Health: {p2deck[p2index].health}")

    while p1deck[p1index].health == 0:
        for i in range(0, 3):
            print(f"{i}: {p1deck[i].name}")
        p1index = int(input("P1 choose your pokemon: "))
    
    while p2deck[p2index].health == 0:
        for i in range(0, 3):
            print(f"{i}: {p2deck[i].name}")
        p2index = int(input("P2 choose your pokemon: "))

    print(f"Player {turn}, it is your turn:")
    print("1: Attack")
    print("2: Swap")
    option = input("Enter option: ")
    if option == "1":
        #print the attack
        for i in range(0, 3):
            if turn == 1:
                print(f"Name: {p1deck[p1index].attacks[i].name}, Damage: {p1deck[p1index].attacks[i].damage}, Crit Chance: {p1deck[p1index].attacks[i].critChance}, Uses: {p1deck[p1index].attacks[i].uses}")
            if turn == 2:
                print(f"Name: {p2deck[p2index].attacks[i].name}, Damage: {p2deck[p2index].attacks[i].damage}, Crit Chance: {p2deck[p2index].attacks[i].critChance}, Uses: {p2deck[p2index].attacks[i].uses}")
        
        attackIndex = int(input("Enter attack number: "))
        if turn == 1:
            turnDamage = getDamage(p2index, p2deck, p1index, p1deck, attackIndex)
            print(f"Player 2 took {turnDamage} damage.")
        if turn == 2:
            turnDamage = getDamage(p1index, p1deck, p2index, p2deck, attackIndex)
            print(f"Player 1 took {turnDamage} damage.")
    
    if option == "2": 
        if turn == 1:
            for i in range(0, 3):
                print(f"{i}: {p1deck[i].name}")
            p1index = int(input("P1 choose your pokemon: "))
        if turn == 2:
            for i in range(0, 3):
                print(f"{i}: {p2deck[i].name}")
            p2index = int(input("P2 choose your pokemon: "))

    if turn == 1:
        turn = 2
    else:
        turn = 1
