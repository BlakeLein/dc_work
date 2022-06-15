from random import randint
class Character:
    def __init__(self, name="", power=0, currentHp=0, maxHp=0, sneak=0, items=[], equipment=[]):
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
        self.lookAround4 = False
        self.specialAction1 = False
        self.specialAction2 = False
        self.specialAction3 = False
        self.useItem1 = False
        self.useItem2 = False
        self.useItem3 = False

        


class Plurn:
    def __init__(self):
        self.player = Character("name", 5, 5, 20, 10)
        self.grek = Character("Pirate Grek", 2, 15, 15, 0)
        self.scene1 = True
        self.scene2 = False
        self.scene3 = False
        self.battle = True

    def displayStats(self):
        # for item in self.player.items:
        #     formitems = print(item)
        print(f'''
    |||| NAME: {self.player.name}
    |||| RANK: P.L.U.R.N. Space Cadet
    |||| <<Hit Points>>
    |||| {self.player.currentHp} / {self.player.maxHp}
    |||| <<Items>>                                   
    |||| {self.player.items}
    |||| <<Equipped Items>>
    |||| {self.player.equipment}
    ''')

    def gameOver(self):
        print('''
    Game Over. You lose.
    ''')
        self.scene1 = False
        self.scene2 = False
        self.scene3 = False

    def rest(self):
        if self.player.currentHp < self.player.maxHp:
            print('''
    You find a dark corner and sit for a while. You assess your wounds and do what
    you can to patch yourself up.
    ''')
            self.player.currentHp = self.player.maxHp
        else:
            print('''
    You don't need to rest.
    ''')

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
    
    def scene1LookAround(self):
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
            self.player.equipment.append("metal pipe")
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
            self.player.equipment.append("soft shoes")
            self.player.sneak += 5

            print('''
    As you turn to your right, you see her lifeless body strapped to a seat. Pam. You've known her since you
    both joined up, and now she's gone while you keep going. She managed to don a kevlar space vest during the
    evacuation sequence. You have to press forward, and you may need that vest if pirates are involved.
    ''')
            self.player.equipment.append("kevlar vest")
            self.player.maxHp += 5
            self.player.currentHp = self.player.maxHp
            self.player.lookAround3 = False
            self.player.specialAction2 = True

        elif self.player.lookAround4 == True:
            print('''
    Feeling hopeless you go to the viewport to take another look at the constellations you used to dream about
    as a child. Your escape pod has enough oxygen for a few more hours, and then you'll slowly slip into a deep
    sleep you cannot wake up from.

    Then you see it again. The Pirate ship is floating slowly aross your view, and you notice the docking bay is
    wide open. If you could time it perfectly, you could use what fuel remains in the pod to jetison into
    the docking bay of the other ship.

    You quickly make your way to the console and initialize the engine thrust sequence. You only have one shot.
    ''')
            guess = 0
            while guess > 5 or guess < 1:
                guess = int(input('''
    (Pick a number between 1 and 5)
    '''))
            failure = randint(1, 5)
            if guess == failure:
                print('''
    You close your eyes and wait a couple seconds. You mash the thrust button, and as the pod lurches forward.
    The P.L.U.R.N. pod sails past the Pirate ship - you were not even close...
    ''')
                self.gameOVer()
                self.scene1 = False

            else:
                print('''
    You close your eyes and wait a couple seconds. You mash the thrust button, and as the pod lurches forward.
    The P.L.U.R.N. pod looks as if it will continue into empty space, but narrowly hits the side of the
    docking bay window. As the shuttle begins to rapidly spin, it makes it into the bay and slams into a panel
    on the wall. The docking bay doors slam shut and the ship's artificial gravity takes hold. You fall to the
    floor and the air is knocked from your lungs. Over the sound of oxygen rushing into the docking bay, you hear
    two men running toward your ship...
    ''')
                print('''
    Now for the next problem...
    ''')
                plurn.scene2 = True
                plurn.scene1 = False

        else: 
            print('''
    You have already looked around the capsule.
    ''')

    def scene1SpecialAction(self):
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
                    self.gameOver()
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
            print('''
    You go over to the main terminal again. You see the options displayed across the screen.
    ''')
            proceed = ''
            while proceed != 'y':
                choice2 = input('''
        What option do you select?
            1. Escape Pod Diagnostics
            2. Escape Pod Logs
            3. Escape Pod Functions
        ''')
                if choice2 == "1":
                    print('''
        OCCUPANTS: 2
        OXYGEN LEVELS: 46%
        LIFE SUPPORT STATUS: Stable
        FUEL LEVEL: 5%
        MANEUVERABILITY: Disabled
        HYDERDRIVE: Decomissioned
        SIGNAL TO PLURNING STAR: ---
        ''')
                if choice2 == "2":
                    print('''
        NO LOGS TO DISPLAY.
        ''')
                if choice2 == "3":
                    print('''
        ESCAPE POD FUNCTIONS:
        - Self Destruct
        - Engine Thrust
        - Jetison Fuel
        ''')
                    print('''
    You realize the escape pod has no way to steer. Other than a quick rear-engine thrust that will
    launch you forward, you are dead in the water...
    ''')
                    proceed = 'y'
                    self.player.lookAround4 = True

        else:
            print("You're not sure what to do...")

    def scene1UseItem(self):
        if self.player.useItem1 == False:
            print("You don't have any items worth using right now.")
        if self.player.useItem1 == True:                
            print('''
You float over to the computer and take a closer look. After about 10 minutes of recalling 
your space training and trying not to electricute yourself, you manage to reattach the power
cell. The computer comes to life and the glow of the monitor stings your eyes.

The computer displays the P.L.U.R.N. Space Corps logo along with the taunting motto - 
"A safer world for all mankind." Some motto. You see a login menu for a P.L.U.R.N. Officer to
sign in. You don't have such credentials. The only way in is by force.
''')
            self.player.items.remove('power cell')
            self.player.useItem1 = False
            self.player.lookAround2 = True

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
            self.scene1LookAround()

        if action == "2":
            self.displayStats()
        
        if action == "3":
            self.scene1SpecialAction()

        if action == "4":
            self.scene1UseItem()

        if action == "5":
            self.rest()

    def sceneTwoOpen(self):
        print('''
    You get to your feet in time to see two hulking Bausten Pirates burst through the door with electro-batons
    crackling. You grab your metal rod and charge the first one.
    ''')
    
    def battleOne(self):
        while self.battle != True:
            self.checkHealth()
            self.b1PlayerAttack()
            self.checkHealth()
            self.b1EnemyAttack()
            self.checkHealth()

    def b1PlayerAttack(self):
        attack = ''
        while attack != '1' and attack != '2' and attack != '3':
            attack = input('''
    Battle! What would you like to do?
        1. Attack
        2. Check Stats
        3. Drop your weapon and give up...
    ''')
            if attack == '1':
                damage = randint(1, self.player.power)
                print(f'''
    You swing your weapon with force at {self.grek.name}! You deal {damage} points
    of damage!
    ''')
                self.grek.currentHp -= damage

            elif attack == '2':
                self.displayStats()
                self.b1PlayerAttack()

            elif attack == '3':
                confirm = ''
                while confirm != '1' and confirm != '2':
                    confirm = input('''
    Are you...sure...you want to do that?
        1. Absolutely
        2. Nevermind
    ''')
                    if confirm == '1':
                        print('''
    You lay down your weapon and the enemy overtakes you...
    ''')
                        self.gameOver()
                    elif confirm == '2':
                        self.b1PlayerAttack()

    def checkHealth(self):
        if self.player.currentHp <= 0:
            print('''
    The enemy takes a swing and hits you square in temple. Your vision goes black, and the
    world goes cold...
    ''')
            self.gameOver()

        if self.grek.currentHp <= 0:
            print(f'''
    You bash {self.grek.name} across the face and he falls lifeless.
    ''')
            self.battle = False
            
        
    def b1EnemyAttack(self):
        damage = randint(1, self.grek.power)
        print(f'''
    {self.grek.name} snarls and swings wildly at you. You take {damage} points
    of damage!
    ''')
        self.player.currentHp -= damage


# Create instance of game class
plurn = Plurn()

# Start Game
plurn.openingSceneGetName()

# Main Game Loops
while plurn.scene1 == True:
    plurn.sceneOne()

while plurn.scene2 == True:
    print("Here's scene 2!")
    break

while plurn.scene3 == True:
    print("Here's scene 3!")
    break
2
