from random import randint
from time import sleep
import sys
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
        self.player = Character("name", 5, 15, 20, 10, [''], ['metal pipe'])
        self.grek = Character("Pirate Grek", 5, 15, 15, 0)
        self.commander = Character("Commander Matthew", 9, 20, 20, 0)
        self.scene1 = True
        self.scene2 = True
        self.scene3 = False
        self.battle1 = True
        self.battle2 = False

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
        sys.exit()

    def resetFlags(self):
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
    look more comfortable than the ones you have on. You decide to put them on. 
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
                self.gameOver()
                

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
                self.resetFlags()
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
    credentials. You begin to cry, but then you remember that every P.L.U.R.N. Corps computer has a secret back 
    door: the Riddle Matrix! Of course!

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
        the sign post. "Please traveler" the goblin rasps. "Help me cure my wounds so I may return to my family."

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
            print('''
    You're not sure what to do...
    ''')

    def scene1UseItem(self):
        if self.player.useItem1 == True:                
            print('''
You float over to the computer and take a closer look. After about 10 minutes of recalling 
your space training and trying not to electrocute yourself, you manage to reattach the power
cell. The computer comes to life and the glow of the monitor stings your eyes.

The computer displays the P.L.U.R.N. Space Corps logo along with the taunting motto - 
"A safer world for all mankind." Some motto. You see a login menu for a P.L.U.R.N. Officer to
sign in. You don't have such credentials. The only way in is by force.
''')
            self.player.items.remove('power cell')
            self.player.useItem1 = False
            self.player.lookAround2 = True

        else:
            print('''
    You don't have any items worth using right now.
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
        while self.battle1 == True:
            self.b1PlayerAttack()
            sleep(2)
            self.b1CheckHealth()
            sleep(2)
            if self.battle1 == True:
                sleep(2)
                self.b1EnemyAttack()
                sleep(2)
                self.b1CheckHealth()
                sleep(2)
        print('''
    You finish off the Bausten Pirate thug, and it looks like no one heard or saw you. You should be sneaky...
        ''')

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

    def b1CheckHealth(self):
        if self.player.currentHp <= 0:
            print('''
    The enemy takes a swing and hits you square in temple. Your vision goes black, and the
    world goes cold...
    ''')    
            self.gameOver()

        elif self.grek.currentHp <= 0:
            print(f'''
    You bash {self.grek.name} across the face and he falls lifeless.
    ''')
            self.battle1 = False

        else:
            self.displayStats()      
        
    def b1EnemyAttack(self):
        damage = randint(1, self.grek.power)
        print(f'''
    {self.grek.name} snarls and swings wildly at you. You take {damage} points
    of damage!
    ''')
        self.player.currentHp -= damage

    def sceneTwo(self):
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
            self.scene2LookAround()

        if action == "2":
            self.displayStats()
        
        if action == "3":
            self.scene2SpecialAction()

        if action == "4":
            self.scene2UseItem()

        if action == "5":
            self.rest()

    def scene2LookAround(self):
        if self.player.lookAround1 == False:
            print('''
    You walk over to the pirate and check his pulse. Dead. You notice his weapon was damaged beyond
    in the battle. You do notice his key card in his satchel, and decide to take that...
    ''')
            self.player.items.append("pirate key card")
            print('''
    Now that you think of it, the pirate is generally the same size as you. You think it might be a good
    idea to put on his clothes...maybe it will be a nice disguise?
    ''')
            disguise = ''
            while disguise != '1' and disguise != '2':
                disguise = input('''
    Do you put on the pirate's outfit?
        1. Yeah, duh.
        2. No, that's gross.
    ''')
            if disguise == '1':
                print('''
    You take a couple minutes to put on the pirate's clothes and practice your best pirate voice. You've got this.
    ''')
                caught = randint(1, 5)
                if caught == 3:
                    print('''
    As you are putting on the smelly garb, another pirate comes up behind you and clubs you on the head. Why
    did you think it was a good idea to change outfits in the middle of an enemy ship?
    ''')
                    self.gameOver()
                
                else:
                    print('''
    You successfully put on the pirate's clothes, and you look terrible! Perfect! Maybe this will
    fool any other pirates you come across.
    ''')
                    self.player.equipment.append('pirate clothes')
                    self.player.sneak += 5
            
            elif disguise == '2':
                print('''
    Why would you put on a discguise in the middle of an enemy ship? You carefully drag the pirate's body behind
    a crate in a dark corner and leave him.
    ''')
            self.player.lookAround1 = True
            self.player.lookAround2 = True
        
        elif self.player.lookAround2 == True:
            print('''
    You take a moment to survey the situation. You are standing alone in a docking bay with a destroyed ship in
    one corner and a dead pirate in the other corner. For some strange reason, no one has come running to the
    bay as a result of an escape pod crashing into it...
    ''')
            print('''
    You know that a ship this size has a hyperdrive. Maybe you can get to the bridge, seal yourself in, and make
    the jump to earth. From there you could fly to Plurnquarters and help bring these pirates to justice.
    ''')
            self.player.lookAround2 = False
            self.player.specialAction1 = True
            self.player.useItem1 = True

        elif self.player.lookAround3 == True:
            print('''
    You notice the Commander has a really neat helmet. Man that helmet looks neat. 'Mine!'
    ''')
            self.player.equipment.append('pirate helmet')
            self.player.currentHp += 5
            self.player.maxHp += 5
            self.player.lookAround3 = False
            self.player.lookAround4 = True

            print('''
    You step over the Commander's helmetless corpse and make your way to another security door in the hallway.
    You flash your key card and it snaps open.
    ''')

        elif self.player.lookAround4 == True:
            print('''You are standing in a small room with another door
    right in front of you. Based on your feel for the layout of this vessel, you know that you are looking
    at the door to the bridge...
    ''')
            print('''
    Almost home.
    ''')
            print('''
    You ready yourself with weapon drawn and creep toward the door.
    ''')
            print('''
    It's so quiet. You no longer hear the hustle and bustle of pirates scrambling to find you. Were they looking
    for you? Or someone else?
    ''')
            self.scene3 = True
            self.scene2 = False
        else: 
            print('''
    You have already looked around the capsule.
    ''')

    def scene2SpecialAction(self):
        if self.player.specialAction1 == True:
            print('''
    You look into the crate obscurring the dead pirate and find a few blaster rifles. You have never been more elated
    in your entire life. You grab one and throw the metal pipe across the room.
    ''')
            self.player.equipment.remove('metal pipe')
            self.player.equipment.append('blaster rifle')
            self.player.power += 3
            self.player.specialAction1 = False

        elif self.player.specialAction2 == True:
            print('''
    You poke your head through the now open door and swipe it side to side. On your left is a dead-end. On your right 
    is a man staning a head taller than the average man with a large gun strapped to his back. He is talking to another
    and you hear him referred to as 'Commander.'
    ''')
            print('''
    So this is the one in charge. The one you have to worry about. You slink back and listen to them talk.
    ''')
            print('''
    "The wreckage was here when we arrived my Lord. We picked up the debris and figured we could be the first to scavenge.
    We didn't expect- "
    ''')
            print('''
    "Of course you didn't expect them fool! They only arrived moments ago. Do you have any updates for me? What
    happened to the one we picked up on the scanners?!"
    ''')
            print('''
    "Still looking my lord. We have not seen it since for several minutes. We did scramble the crew, but many of 
    them have given up.
    ''')
            print('''
    You realize that something is wrong, but all you can think about is getting to the bridge. You study the Commander 
    as he talks to his subordinant.
    ''')
            option = ''
            while option != '1' and option != '2':
                option = input('''
    What would you like to do?
        1. Attempt to sneak past the guard.
        2. Raise your weapon and run in like a crazy person.
    ''')
            if option == '1':
                print('''
    You settle your equipment and carefully step out. You see another door 10 feet down the hall on the left side.
    ''')
                sneak = randint(1, 21)
                if self.player.sneak >= sneak:
                    print('''
    You slowly put one foot in front of the other and make your way to the second door. You discreetly flash the key
    card and re-enter the password. As the door hisses open you see the Commanders head start to turn, but not before
    you are able to slam it shut and blast the panel. They won't be following you.
    ''')
                    self.player.specialAction2 = False
                    self.player.lookAround4 = True
                else:
                    print('''
    You slowly put one foot in front of the other and make your way to the second door. After a few steps, the
    Commander whips his head around and raises his blaster before you can react. You feel an impossibly hot pain
    in your chest as the world goes dark.
    ''')
                    self.battle2 = True
                    self.battleTwo()
                    print('''
    You finish off the Commander with gusto. He didn't even have a name tag; he had no chance.
    ''')
                    self.player.specialAction2 = False
                    self.player.lookAround3 = True

            elif option == '2':
                print('''
    You raise your weapon and scream. Your voice jumps to a higher octave than you expect it to. The grunt standing
    next to the Commander screams even higher and runs away.
    ''')
                print('''
    The Commander raises his rifle and aims for your chest. You barrel-roll to the right and feel the hot light 
    flash inches from your left eye. You raise your weapon...
    ''')
                self.battle2 = True
                self.battleTwo()
                print('''
    You finish off the Commander with gusto. He didn't even have a name tag; he had no chance.
    ''')
                self.player.specialAction2 = False
                self.player.lookAround3 = True

        else:
            print('''
    You're not sure what to do...
    ''')

    def battleTwo(self):
        while self.battle2 == True:
            self.b2PlayerAttack()
            sleep(2)
            self.b2CheckHealth()
            sleep(2)
            if self.battle2 == True:
                sleep(2)
                self.b2EnemyAttack()
                sleep(2)
                self.b2CheckHealth()
                sleep(2)

    def scene2UseItem(self):
        if self.player.useItem1 == True:
            print('''
    You locate the security door that leads to a hallway. At the side of the door is a key pad. You swipe the pirate's
    key card and a message appears on the screen:
    ''')
            print('''
            USER: Grek
            RANK: Grunt
            RATING: 3/10
            
            To proceed, please enter your password:
    ''')

            hack = ''
            while hack != '1' and hack != '2':
                hack = input('''
                1. You type in 'password'
                2. You type in '12345'
''')
            if hack == '1' or hack == '2':
                print('''
    You easily guess the fool's password and the door slides open with a cool hiss.
    ''')
            self.player.useItem1 = False
            self.player.specialAction1 = False
            self.player.specialAction2 = True
        else:
            print('''
    You don't have any items worth using right now.
    ''')

    def b2PlayerAttack(self):
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
    You swing your weapon with force at {self.commander.name}! You deal {damage} points
    of damage!
    ''')
                self.commander.currentHp -= damage

            elif attack == '2':
                self.displayStats()
                self.b2PlayerAttack()

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
                        self.b2PlayerAttack()
    
    def b2EnemyAttack(self):
        damage = randint(1, self.commander.power)
        print(f'''
    {self.commander.name} snarls and swings wildly at you. You take {damage} points
    of damage!
    ''')
        self.player.currentHp -= damage

    def b2CheckHealth(self):
        if self.player.currentHp <= 0:
            print('''
    The enemy takes a swing and hits you square in temple. Your vision goes black, and the
    world goes cold...
    ''')    
            self.gameOver()

        elif self.commander.currentHp <= 0:
            print(f'''
    You bash {self.commander.name} across the face and he falls lifeless.
    ''')
            self.battle2 = False

        else:
            self.displayStats()  


# Create instance of game class
plurn = Plurn()

# Start Game
# plurn.openingSceneGetName()

# Main Game Loops
########### Scene 1 ###########
# while plurn.scene1 == True:
#     plurn.sceneOne()

########### Scene 2 ###########
# plurn.battleOne()
while plurn.scene2 == True:
    plurn.sceneTwo()
    

########### Scene 3 ###########
# while plurn.scene3 == True:
#     print("Here's scene 3!")
#     break
# 2
