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
                                                        Attack("Hydro Pump", 40, 0.5, 2)])]

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

def getDamage(index: int, deck: list, attack: int):
    #placeholder return
    return 10

def doDamage(damage: int, index: int, deck: list):
    #finish code, void function

print(p1deck)
p1index = int(input("P1 choose your pokemon: "))
print(p2deck)
p2index = int(input("P2 choose your pokemon: "))
turn = 1

option = ""
while isWin() == 0:
    #print pokemon status for both players
    print("1: Attack")
    print("2: Swap")
    option = input("Enter option: ")
    if option == "1":
        #print the attack
        attackIndex = int(input("Enter attack number: "))
        if turn == 1:
            turnDamage = getDamage(p1index, p1deck, attackIndex)
            print(f"Player 2 took {turnDamage} damage.")
            doDamage(turnDamage, p2index, p2deck)
        if turn == 2:
            turnDamage = getDamage(p2index, p2deck, attackIndex)
            print(f"Player 1 took {turnDamage} damage.")
            doDamage(turnDamage, p1index, p1deck)
    
    if option == "2": 
        if turn == 1:
            print(p1deck)
            p1index = int(input("P1 choose your pokemon: "))
        if turn == 2:
            print(p2deck)
            p2index = int(input("P2 choose your pokemon: "))

    if turn == 1:
        turn = 2
    else:
        turn = 1
