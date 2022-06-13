class Character:
    def __init__(self, name="", power=0, currentHP=0, maxHp=0, sneak=0, items=[]):
        self.name = name
        self.power = power
        self.currentHP = currentHP
        self.maxHp = maxHp
        self.sneak = sneak
        self.items = items


class Plurn:
    def __init__(self):
        self.player = Character("name", 5, 5, 20, 10)

        
    def openingSceneGetName(self):
        print('''
        Your eyes slowly open. You are weightless in a small capsule
        floating in space. A faint light flashes. There is the faint glow
        of the local sun coming through the small viewport.
        ''')

        self.player.name = input('''
        Do you remember your name?

        >>> 
        ''').title()

        print(f'''
        Yes it's all coming back to you. Your name is {self.player.name}.
        You are a member of the P.L.U.R.N. Space Corps. 
        ''')
    

    def sceneOnePartOne(self):
        
        action = input('''
        What would you like to do?
        1. Look through view port.
        2. Look around capsule.

        >>> 
        ''')
        while action != "1" and action != "2" and action != "3" and action != "4" and action != "5":
            
            action = input('''
        What would you like to do?
        1. Look Through View Port.
        2. Look Around.
        3. Check Inventory.
        4. Use Item.
        5. Rest.

            >>> 
            ''')
        if action == "1":
            print('''
        As you clamber over to the small viewport, you see the stars outside slowly spinning.
        There is a sea of twisted metal and debris floating all around you. You make out a metal
        plate with a charred P.L.U.R.N. crest. You recognize this as the same crest from your ship - 
        "The Plurning Star." Where is your ship?
            ''')
        if action == "2":
            print('''
        
            ''')

            



plurn = Plurn()

plurn.openingSceneGetName()
plurn.sceneOnePartOne()


