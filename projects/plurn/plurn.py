class Character:
    def __init__(self, name="", power=0, currentHp=0, maxHp=0, sneak=0, items=[], equipment=[None]):
        self.name = name
        self.power = power
        self.currentHp = currentHp
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
        self.scene1 = True
        self.scene2 = False
        self.scene3 = False

    def displayStats(self):
        print(f'''
    |||| <<Hit Points>>                               
    |||| {self.player.currentHp} / {self.player.maxHp}       
    |||| <<Items>>                                   
    |||| {self.player.items}
    |||| <<Equipped Items>>
    |||| {self.player.equipment}                       
        ''')

    def gameOVer(self):
        print('''
    Game Over. You lose.
        ''')

    def rest(self):
        if self.player.currentHp < self.player.maxHp:
            print('''
    You find a dark corner and sit for a while. You assess your wounds and do what
    you can to patch yourself up.
        ''')
            self.player.currentHp = self.player.maxHp
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
    Yes, you remember. Your name is {self.player.name}.
    You are a member of the P.L.U.R.N. Space Corps. 
        ''')
    

    def sceneOne(self):
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
            if self.player.lookAround1 == False:
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
                self.player.items.append('power cell')
                self.player.power += 2
                self.player.lookAround1 = True
                self.player.useItem1 = True

            elif self.player.lookAround2 == True:
                print('''
    Through the view port you see another ship come into view. It's too small to be a transport and
    by the looks of the large sonic blasters outfitted on the side, you know that this ship was
    built for one purpose - destruction. It's filthy and unkept, and on the sides above the rear
    thrusters, you see the blood-red sun surrounded by black flames. You recognize this as the logo
    of the Bausten Pirate Syndicate.
                ''')
                self.player.lookAround2 = False
                self.player.specialAction1 = True

            elif self.player.lookAround3 == True:
                print('''
    You decide to take another glance around the pod with the lights back on. You find a pair of shoes that
    look for comfortable than the ones you have on. You decide to put them on. 
                ''')
                self.player.equipment[1] = "soft shoes"
                self.player.sneak += 5

                print('''
    As you turn to your right, you see her lifeless body slumped over a seat. Pam. You've known her since you
    both joined up, and now she's gone while you keep going. She managed to don a kevlar space vest during the
    evacuation sequence. You have to press forward, and you may need that vest if pirates are involved.
                ''')
                self.player.equipment[2] = "kevlar vest"
                self.player.maxHp += 5
                self.player.currentHp = self.player.maxHp
                self.player.lookAround3 = False
            else: 
                print("You have already looked around the capsule.")
        if action == "2":
            self.displayStats()
            
        if action == "3":
            if self.player.specialAction1 == True:
                print('''
    As you float in the P.L.U.R.N. pod, you realize there is no hope for you while the systems remain offline.
    You go back to the computer to see if you can restore power. You know there is no way to guess the login
    credentials, but you that every P.L.U.R.N. Corps computer has a secret back door: the riddle matrix.

    You locate the matrix symbol at the bottom-right of the screen. The stakes couldn't be higher, but
    the circumstances couldn't be more dire. You click the symbol, and the screen goes black.
            ''')
                print('''
        Welcome to Plurn: The Riddles of Queelix! I will ask of you a riddle, and your answer will determine your fate.
                ''')
                choice = ''
                while choice != "1" and choice != "2":
                    choice = input('''
        You are walking down a path on your way to a funeral. You come up to an intersection where a goblin lay against
        the sign post. "Please traveler" the goblin rasps. "Help me cure my wounds so I may return to my family."2

        What do you you do?
        1. Help Goblin. He just wants to see his children again.
        2. Shoot Goblin.
            ''')
                    if choice == "1":
                        print('''
        As you bend over to offer the goblin a helping hand, several more goblins spring forth and stab you to death.
        You were a fool to believe a goblin would ask you for help.
                    ''')
                        print('''
    RIDDLE MATRIX DETECTS INTRUDER. SYSTEM ALERT. IMMEDIATE SELF-DESTRUCT SEQUENCE INITIALIZED.
                    ''')
                        self.gameOVer()
                        self.scene1 = False
                    elif choice == "2":
                        print('''
        Almost before the goblin can finish asking for help, you take your crossbow and give him one between
        the eyes. Everyone knows that goblins hate humans. Several other goblins scatter in a frenzied panic. You
        go ahead and shoot them too.
                    ''')
                        print('''
    The screen goes black for another moment and then fires back to life with a control module displayed. 
    The capsule comes to life. Lights are on and oxygen seeps into the cabin. You have full access 
    to the pod's systems.
                    ''')
                        self.player.specialAction1 = False
                        self.player.lookAround3 = True

            elif self.player.specialAction2 == True:
                pass
            else:
                print("You're not even sure where to begin.")

        if action == "4":
            self.displayStats()
            if self.player.useItem1 == False:
                print("You don't have any items worth using right now.")
            if self.player.useItem1 == True:                
                print( print('''
    You float over to the computer and take a closer look. After about 10 minutes of recalling 
    your space training and trying not to electricute yourself, you manage to reattach the power
    cell. The computer comes to life and the glow of the monitor stings your eyes.

    The computer displays the P.L.U.R.N. Space Corps logo along with the taunting motto - 
    "A safer world for all mankind." Some motto. You see a login menu for a P.L.U.R.N. Officer to
    sign in. You don't have such credentials. The only way in is by force.
            '''))
                self.player.items.remove('power cell')
                self.player.useItem1 = False
                self.player.lookAround2 = True

            
        if action == "5":
            self.rest()
            
            



plurn = Plurn()

plurn.openingSceneGetName()

while plurn.scene1 == True:
    plurn.sceneOne()

# while plurn.scene2 == True:

