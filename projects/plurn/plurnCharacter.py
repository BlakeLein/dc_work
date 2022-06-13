class Character:
    def __init__(self, name, power, maxHp, maxAccuracy):
        self.name = name
        self.power = power
        self.maxHp = maxHp
        self.maxAccuracy = maxAccuracy



def createCharacter():
    print('''
    Your eyes slowly open. You are weightless in a small capsule
    floating in space. An alarm blares and your head is killing you.
    ''')

    name = input('''
    Do you remember your name?

    >>> 
    ''').title()
    
    race = ""
    while race != 1 and race != 2 and race != 3:
        try:
            race = int(input('''
    What was your rank in the Grand Plurn Navy?

    1. Plurn Soldier (Fighter)
    2. Plurn Operative (Rogue)
    3. Plurn Marksmen (Sharpshooter)

    >>> 
        '''))

        except ValueError:
            print("Please Enter 1, 2, or 3.")
        

    if race == 1:
        player = Character(name, 5, 20, 75)
        return player

    if race == 2:
        player = Character(name, 4, 20, 80)
        return player

    if race == 3:
        player = Chracter(name, 3, 20, 85)
        return player


player = createCharacter()
print(player.name)
print(player.power)
print(player.maxHp)
print(player.maxAccuracy)

