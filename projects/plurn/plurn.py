class Character:
    def __init__(self, name="", power=0, currentHp=0, maxHp=0, sneak=0, items=[None], equipment=[None]):
        self.name = name
        self.power = power
        self.currentHP = currentHp
        self.maxHp = maxHp
        self.sneak = sneak
        self.items = items
        self.equipment = equipment
        self.lookAround1 = False
        self.lookAround2 = False
        self.lookAround3 = False
        self.specialAction1 = False
        self.specialAction2 = False
        self.specialAction3 = False
        self.useItem1 = False
        self.useItem2 = False
        self.useItem3 = False


class Plurn:
    def __init__(self):
        self.player = Character("name", 5, 5, 20, 10)

    def displayStats(self):
        print(f'''
    |||| <<Hit Points>>                               
    |||| {self.player.currentHP} / {self.player.maxHp}       
    |||| <<Inventory>>                                   
    |||| {self.player.items}
    |||| <<Equiped Items>>
    |||| {self.player.inventory}                       
        ''')

    def rest(self):
        print('''
    You find a dark corner and sit for a while. You assess your wounds and do what
    you can to patch yourself up.
        ''')
        if self.player.currentHP < self.player.maxHp:
            self.player.currentHP == self.player.maxHp
        else:
            print("You don't need to rest.")



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
    1. Look Around.
    2. Show Stats.
    3. Special Action.
    4. Use Item.
    5. Rest.
    >>>
        ''')
        while action != "1" and action != "2" and action != "3" and action != "4" and action != "5":
            action = input('''
    What would you like to do?
    1. Look Around.
    2. Show Stats.
    3. Special Action.
    4. Use Item.
    5. Rest.
    >>>
            ''')
        if action == "1":
            if self.player.lookAround == False:
                print('''
    You feel your way around the dark capsule. You recognize it as an escape pod. By the looks of the 
    registration number and P.L.U.R.N. Space Corps crest, you know you are in an escape pod for
    your ship - the 'Plurning Star.' You clamber over to the view port and see a field of debris
    amongst the stars. As some pieces rubble float across your capsule, you recognize the twisted metal
    as the meager remnants of your ship.

    You notice in the capsule a thick metal rod, a computer with a blank screen, and a power cell 
    laying on the floor. You decide to loop the metal rod into your space suit's belt loop.
                ''')
                self.player.equipment[0] = ("metal pipe")
                self.player.power += 2
                self.player.specialAction1 = True
                self.player.lookAround = True
            else:
                print("You have already looked around the capsule.")
        if action == "2":
            self.displayStats()
            
        if action == "3":
            if self.player.specialAction1 == True:
                print('''
    You float over to the computer and take a closer look at those loose wires. After about 10 minutes
    of recalling your space training and trying not to electricute yourself, you manage to reattach
    enough of the wires that the computer stabilizes and shows a menu.
            ''')
                self.player.specialAction1 = False
                self.player.specialAction2 = True
            if self.player.specialAction2 == True:

            else:
                ("You're not even sure where to begin.")

        if action == "4":
            self.displayStats()
            item = input('''
    What item would you like to use?
            ''')
            if item == 

        if action == "5":
            self.rest()
            
            



plurn = Plurn()

plurn.openingSceneGetName()
plurn.displayStats()
plurn.sceneOnePartOne()


