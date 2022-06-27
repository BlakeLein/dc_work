# Import Special Functions
import sys
from random import randint
from time import sleep
from cprint import cprint

# Import Other Game Modules
from plurnCharacter import Character
from colors import Colors

class Plurn:
    """Main class for Plurn 1"""
    def __init__(self):
        self.player = Character("name", "person", 1, 1, 1, 1)
        self.enemy1 = Character("Enemy1", "Grunt", 5, 5, 5, 5)
        self.enemy2 = Character("Enemy2", "Grunt", 5, 5, 5, 5)
        self.enemy3 = Character("Enemy3", "Grunt", 5, 5, 5, 5)
        self.enemy4 = Character("Enemy4", "Grunt", 5, 5, 5, 5)
        self.boss = Character("Boss", "Commander", 5, 5, 5, 5)
        
        # Variables to control scenes
        
        self.battle1 = False
        self.battle2 = False

        # Variables to control order of game play
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
    
    # General Game Methods
    def resetFlags(self):
        """Function to quickly reset all tags for game play"""
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

    def displayStats(self):
        """Quickly display the players stats in a
            neat format."""
        print(f'''
    || NAME: {self.player.name} |||| RANK: {self.player.rank} ||

    <<Hit Points>>
        {self.player.currentHp} / {self.player.maxHp}''')
        print('''
    <<Items>>''')                                   
        for i in self.player.items:
            print(f'        {i.title()}')
        print('''
    <<Equipment>>''')
        for e in self.player.equipment:
            print(f'        {e.title()}')

    def rest(self):
        """Heal player if health below max"""
        if self.player.currentHp < self.player.maxHp:
            cprint('''
You find a dark corner and sit for a while. You assess your wounds and do what
you can to patch yourself up.
''')
            self.player.currentHp = self.player.maxHp
            # sleep(2)

        else:     
            cprint('''
You don't need to rest.
''')

    def gameOver(self):
        """End the game."""
        cprint("Game Over")
        # sleep(1)
        cprint("You lose.")
        # sleep(1)
        sys.exit()

    def openingSceneGetName(self):
        """Opening narrative, get name, and get class"""
        cprint('Your eyes slowly open.')
        # sleep(2)
        cprint('You are weightless in a small capsule floating in space.')
        # sleep(2)
        cprint('A light flashes.')
        # sleep(2)
        cprint('There is a faint glow from the local sun.')
        # sleep(2)

        self.player.name = input('''
Do you remember your name?
>>> 
    ''').title()

        # sleep(1)
        cprint(f'Yes, you remember. Your name is {self.player.name}.')
        # sleep(2)
        cprint('You are a member of the P.L.U.R.N. Space Corps.')
        # sleep(2)
        rank = ''
        while rank != '1' and rank != '2' and rank != '3':
            rank = input('''
Do you remember your rank?
    
    1. Soldier (+ Attack, + Health, - Sneak)
    2. Operative (+ Attack, - Health, + Sneak)
    3. Medic (- Attack, + Health, + Sneak)
>>>
''')
        if rank == '1':
            self.player = Character(f"{self.player.name}", 'P.L.U.R.N. Corps Soldier', 6, 1, 22, 3)

        elif rank == '2':
            self.player = Character(f"{self.player.name}", 'P.L.U.R.N. Corps Operative', 6, 1, 15, 10)

        elif rank == '3':
            self.player = Character(f"{self.player.name}", 'P.L.U.R.N. Corps Medic', 4, 1, 25, 10)

    def closingScene(self):
        """Final narration"""
        # sleep(2)
        cprint('.....')
        # sleep(2)
        cprint('.....')
        # sleep(2)
        cprint('''
Your eyes open. You are badly injured.
''')
        sleep(4)
        cprint('.....')
        # sleep(2)
        cprint('.....')
        # sleep(2)
        cprint('''
You are in your base clothes and bound by an organic substance in a dark room. You 
guess you are aboard the alien ship.
''')
        sleep(5)
        cprint('.....')
        # sleep(2)
        cprint('.....')
        # sleep(2)
        cprint('''
You are tired and all out of hope. You no longer fear death.
''')
        sleep(4)
        cprint('.....')
        # sleep(2)
        cprint('.....')
        # sleep(2)
        cprint('''
You slowly close your eyes and feel yourself slipping back into a deep sleep. As your body
slowly goes limp, you feel nothing but despair...
''')
        sleep(6)
        cprint('.....')
        # sleep(2)
        cprint('.....')
        # sleep(2)
        cprint('''
...and the icy presence of a metal sphere.
''')


class SceneOne:
    def __init__(self):
        self.scene1 = True
        
    def sceneOne(self):
        """Main actions for Scene 1"""
        action = ''
        while action != "1" and action != "2" and action != "3" and action != "4" and action != "5" and action != '6':
            action = input('''
What would you like to do?
1. Look Around.     3. Special Action.      5. Rest.
2. Show Stats.      4. Use Item.            6. Give up.
>>>
''')
        if action == "1":
            # sleep(1)
            self.scene1LookAround()

        if action == "2":
            # sleep(1)
            Plurn.displayStats()
        
        if action == "3":
            # sleep(1)
            self.scene1SpecialAction()

        if action == "4":
            # sleep(1)
            self.scene1UseItem()

        if action == "5":
            # sleep(1)
            Plurn.rest()
        
        if action == "6":
            confirm = ''
            while confirm != '1' and confirm != '2':
                confirm = input('''
Are you sure you want to give up?
1. Yes
2. No way!
''')
            if confirm == '1':
                # sleep(1)
                Plurn.gameOver()

            elif confirm == '2':
                # sleep(1)
                self.sceneOne()

    def scene1LookAround(self):
        """Controls order of all 'look around' actions in scene 1."""
        if self.lookAround1 == False:
            cprint('''
You feel your way around the dark capsule. It looks like an an escape pod. By the looks of the 
registration number and P.L.U.R.N. Space Corps crest, you know you are in an escape pod for
your ship - the 'Plurning Star.'
''')
            # sleep(5)
            cprint('''
You clamber over to the viewport and see a field of debris amongst the stars. As some pieces of rubble 
float across your capsule, you recognize the twisted metal as the meager remnants of your ship.
''')
            # sleep(5)
            cprint('''
You notice in the capsule a thick metal rod, a computer with a blank screen, and a power cell 
laying on the floor. You decide to grab the cell and loop the metal rod into your space suit's belt loop.
''')
            self.player.equipment.append("metal pipe")
            self.player.items.append('power cell')
            self.player.power += 2
            self.lookAround1 = True
            self.useItem1 = True

        elif self.lookAround2 == True:
            cprint('''
Through the viewport you see another ship come into view. It's too small to be a transport and
by the looks of the large sonic blasters outfitted on the side, you know that this ship was
built for one purpose - destruction.
''')

            # sleep(4)
            cprint('''
It's filthy and unkept, and on the sides above the rear thrusters, you see the blood-red sun surrounded 
by black flames. You recognize this as the logo of the Bausten Pirate Syndicate.
''')
            # sleep(3)
            self.lookAround2 = False
            self.specialAction1 = True

        elif self.lookAround3 == True:
            cprint('''
You decide to take another glance around the pod with the lights back on. You find a pair of shoes that
look more comfortable than the ones you have on. You decide to put them on. 
''')
            # sleep(4)
            self.player.equipment.append("soft shoes")
            self.player.sneak += 5

            cprint('''
As you turn to your right, you see her lifeless body strapped to a seat. Pam. You've known her since you
both joined up, and now she's gone while you keep going. 
''')
            # sleep(4)
            cprint('''
She managed to don a kevlar space vest during the evacuation sequence. You have to press forward, and you 
may need that vest if pirates are involved.
''')
            # sleep(4)
            self.player.equipment.append("kevlar vest")
            self.player.maxHp += 5
            self.player.currentHp += 5
            self.lookAround3 = False
            self.specialAction2 = True

        elif self.lookAround4 == True:
            cprint('''
Feeling hopeless you go to the viewport to take another look at the constellations you used to dream about
as a child. Your escape pod has enough oxygen for a few more hours, and then you'll slowly slip into a deep
sleep you cannot wake up from.
''')
            # sleep(3)
            cprint('''
Then you see it again. The Pirate ship is floating slowly aross your view, and you notice the docking bay is
wide open. If you could time it perfectly, you could use what fuel remains in the pod to jetison into
the docking bay of the other ship.
''')
            # sleep(4)
            cprint('''
You quickly make your way to the console and initialize the engine thrust sequence. You only have one shot.
''')
            # sleep(2)
            guess = 0
            while guess > 5 or guess < 1:
                try:
                    guess = int(input('''
(Pick a number between 1 and 5)
'''))
                except ValueError:
                    cprint('Please type a number.')
            failure = randint(1, 5)
            if guess == failure:
                # sleep(1)
                cprint('''
You close your eyes and wait a couple seconds. You mash the thrust button, and as the pod lurches forward.
The P.L.U.R.N. pod sails past the Pirate ship - you were not even close...
''')
                self.gameOver()
                

            else:
                cprint('''
You close your eyes and wait a couple seconds. You mash the thrust button, and as the pod lurches forward.
The P.L.U.R.N. pod looks as if it will continue into empty space, but narrowly hits the side of the
docking bay window.
''')
                # sleep(4)
                cprint('''
As the shuttle begins to rapidly spin, it makes it into the bay and slams into a panel on the wall. 
The docking bay doors slam shut and the ship's artificial gravity takes hold. You fall to the floor and 
the air is knocked from your lungs. Over the sound of oxygen rushing into the docking bay, you hear
a pirate running toward your ship...
''')
                # sleep(3)
                cprint('''
Now for the next problem...
''')
                # sleep(1)
                plurn.scene2 = True
                self.resetFlags()
                plurn.battle1 = True
                plurn.scene1 = False

        else: 
            cprint('''
You have already looked around the capsule.
''')

    def scene1SpecialAction(self):
        """Controls order of all 'special actions' in scene 1.."""
        if self.specialAction1 == True:
            cprint('''
As you float in the P.L.U.R.N. pod, you realize there is no hope for you while the systems remain offline.
You go back to the computer to see if you can restore power. You know there is no way to guess the login
credentials. You begin to cry, but then you remember that every P.L.U.R.N. Corps computer has a secret back 
door: 
''')
            # sleep(3)
            cprint('''
The Riddle Matrix! Of course!
''')
            # sleep(2)
            cprint('''
You locate the matrix symbol at the bottom-right of the screen. The stakes couldn't be higher, but
the circumstances couldn't be more dire. You click the symbol, and the screen goes black.
''')
            
            # sleep(2)
            cprint('''
    Welcome to Plurn: The Riddles of Queelix! I will ask of you a riddle, and your answer will determine your fate.
    ''')
            # sleep(1)
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
                    # sleep(1)
                    cprint('''
    As you bend over to offer the goblin a helping hand, several more goblins spring forth and stab you to death.
    You were a fool to believe a goblin would ask you for help.
    ''')
                    # sleep(2)
                    cprint('''
RIDDLE MATRIX DETECTS INTRUDER. SYSTEM ALERT. IMMEDIATE SELF-DESTRUCT SEQUENCE INITIALIZED.
''')
                    # sleep(1)
                    self.gameOver()

                elif choice == "2":
                    # sleep(1)
                    cprint('''
    Almost before the goblin can finish asking for help, you take your crossbow and give him one between
    the eyes. Everyone knows that goblins hate humans. Several other goblins scatter in a frenzied panic. You
    go ahead and shoot them too.
    ''')
                    # sleep(4)
                    cprint('''
The screen goes black for another moment and then fires back to life with a control module displayed. 
The capsule comes to life. Lights are on and oxygen seeps into the cabin. You have full access 
to the pod's systems.
''')
                    self.specialAction1 = False
                    self.lookAround3 = True

        elif self.specialAction2 == True:
            cprint('''
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
                    # sleep(1)
                    cprint('''
    OCCUPANTS: 2
    OXYGEN LEVELS: 8%
    LIFE SUPPORT STATUS: Stable
    FUEL LEVEL: 5%
    MANEUVERABILITY: Disabled
    HYDERDRIVE: Decomissioned
    SIGNAL TO PLURNING STAR: ---
    ''')
                if choice2 == "2":
                    # sleep(1)
                    cprint('''
    NO LOGS TO DISPLAY.
    ''')
                if choice2 == "3":
                    # sleep(1)
                    cprint('''
    ESCAPE POD FUNCTIONS:
    - Self Destruct
    - Engine Thrust
    - Jetison Fuel
    ''')
                    
                    # sleep(3)
                    cprint('''
You realize the escape pod has no way to steer. Other than a quick rear-engine thrust that will
launch you forward, you are dead in the water...
''')
                    proceed = 'y'
                    self.specialAction2 = False
                    self.lookAround4 = True

        else:
            cprint('''
You're not sure what to do...
''')

    def scene1UseItem(self):
        """Controls order of all 'usse item' actions in scene 1."""
        if self.useItem1 == True:                
            cprint('''
You float over to the computer and take a closer look. After about 10 minutes of recalling 
your space training and trying not to electrocute yourself, you manage to reattach the power
cell. The computer comes to life and the glow of the monitor stings your eyes.
''')

            # sleep(4)
            cprint('''
The computer displays the P.L.U.R.N. Space Corps logo along with the taunting motto - 
"A safer world for all mankind." Some motto. You see a login menu for a P.L.U.R.N. Officer to
sign in. You don't have such credentials. The only way in is by force.
''')
            # sleep(4)
            self.player.items.remove('power cell')
            self.useItem1 = False
            self.lookAround2 = True

        else:
            cprint('''
You don't have any items worth using right now.
''')

class SceneTwo:
    def __init__(self):
        self.scene2 = False

    def sceneTwoOpen(self):
        """Transitions from Scene 1 to Scene 2"""
        cprint('''
You get to your feet in time to see a hulking Bausten Pirate burst through the door with an electro-baton
crackling. You grab your metal pipe and charge the first one.
''')

    def sceneTwo(self):
        """Main actions for Scene 1"""
        action = ''
        while action != "1" and action != "2" and action != "3" and action != "4" and action != "5" and action != '6':
            action = input('''
What would you like to do?
1. Look Around.     3. Special Action.      5. Rest.
2. Show Stats.      4. Use Item.            6. Give up.
>>>
''')
        if action == "1":
            # sleep(1)
            self.scene2LookAround()

        if action == "2":
            # sleep(1)
            self.displayStats()
        
        if action == "3":
            # sleep(1)
            self.scene2SpecialAction()

        if action == "4":
            # sleep(1)
            self.scene2UseItem()

        if action == "5":
            # sleep(1)
            self.rest()
        
        if action == "6":
            confirm = ''
            while confirm != '1' and confirm != '2':
                confirm = input('''
Are you sure you want to give up?
1. Yes
2. No way!
''')
            if confirm == '1':
                # sleep(1)
                Plurn.gameOver()

            elif confirm == '2':
                self.sceneTwo()

    def scene2LookAround(self):
        """Controls order of all 'look around' actions in scene 2."""
        if self.player.lookAround1 == False:
            cprint('''
You walk over to the pirate and check his pulse. Dead. You notice his weapon was badly damaged
in the battle. You do notice a key card in his satchel, and decide to take that...
''')
            # sleep(4)
            self.player.items.append("pirate key card")
            cprint('''
Now that you think of it, the pirate is generally the same size as you. You think it might be a good
idea to put on his clothes...maybe it will be a nice disguise?
''')
            # sleep(3)
            disguise = ''
            while disguise != '1' and disguise != '2':
                disguise = input('''
Do you put on the pirate's outfit?
    1. Yeah, duh.
    2. No, that's gross.
''')
            if disguise == '1':
                # sleep(1)
                cprint('''
You take a couple minutes to put on the pirate's clothes and practice your best pirate voice. You've got this.
''')
                caught = randint(1, 5)
                if caught == 3:
                    # sleep(1)
                    cprint('''
As you are putting on the smelly garb, another pirate comes up behind you and clubs you on the head. Why
did you think it was a good idea to change outfits in the middle of an enemy ship?
''')
                    # sleep(4)
                    self.gameOver()
                
                else:
                    cprint('''
You successfully put on the pirate's clothes, and you look terrible! Perfect! Maybe this will
fool any other pirates you come across.
''')
                    # sleep(4)
                    self.player.equipment.append('pirate clothes')
                    self.player.sneak += 5
            
            elif disguise == '2':
                cprint('''
Why would you put on a discguise in the middle of an enemy ship? You carefully drag the pirate's body behind
a crate in a dark corner and leave him.
''')
                # sleep(3)
            self.player.lookAround1 = True
            self.player.lookAround2 = True
        
        elif self.player.lookAround2 == True:
            cprint('''
You take a moment to survey the situation. You are standing alone in a docking bay with a destroyed ship in
one corner and a dead pirate in the other corner. For some strange reason, no one has come running to the
bay as a result of an escape pod crashing into it...
''')
            # sleep(5)
            cprint('''
You know that a ship this size has a hyperdrive. Maybe you can get to the bridge, seal yourself in, and make
the jump to earth. From there you could fly to Plurnquarters and help bring these pirates to justice.
''')
            # sleep(4)
            self.player.lookAround2 = False
            self.player.specialAction1 = True
            self.player.useItem1 = True

        elif self.player.lookAround3 == True:
            cprint('''
You notice the Commander has a really neat helmet. Man that helmet looks neat. 'Mine!'
''')
            # sleep(2)
            self.player.equipment.append('pirate helmet')
            self.player.currentHp += 5
            self.player.maxHp += 5
            self.player.lookAround3 = False
            self.player.lookAround4 = True

            cprint('''
You step over the Commander's helmetless corpse and make your way to another security door in the hallway.
You flash your key card and it snaps open.
''')

        elif self.player.lookAround4 == True:
            cprint('''
You are standing in a small room with another door right in front of you. Based on your feel for the 
layout of this vessel, you know that you are looking at the door to the bridge...
''')
            # sleep(4)
            cprint('''
Almost home.
''')
            # sleep(1)
            cprint('''
It's so quiet. You no longer hear the hustle and bustle of pirates scrambling to find you. Were they looking
for you? Or someone else?
''')

            # sleep(4)
            cprint('''
You ready yourself with weapon drawn and creep toward the door.
''')
            # sleep(1)
            self.scene3 = True
            self.player.resetFlags()
            self.scene2 = False

        else: 
            cprint('''
You have already looked around.
''')

    def scene2SpecialAction(self):
        """Controls order of all 'special actions' in scene 2."""
        if self.player.specialAction1 == True:
            cprint('''
You look into the crate obscurring the dead pirate and find a few blaster rifles. You have never been more elated
in your entire life. You grab one and throw the metal pipe across the room.
''')
            self.player.equipment.remove('metal pipe')
            self.player.equipment.append('blaster rifle')
            self.player.power += 3
            self.player.specialAction1 = False

        elif self.player.specialAction2 == True:
            cprint('''
You poke your head through the now open door and swipe it side to side. On your left is a dead-end. On your right 
is a man standing a head taller than the average man with a large gun strapped to his back. He is talking to another
and you hear him referred to as 'Commander.'
''')
            # sleep(5)
            cprint('''
So this is the one in charge. The one you have to worry about. You slink back and listen to them talk.
''')
            # sleep(4)
            cprint('''
"The wreckage was here when we arrived my Lord. We picked up the debris and figured we could be the first to scavenge.
We didn't expect- "
''')
            # sleep(4)
            cprint('''
"Of course you didn't expect them fool! Do you have any meaningful updates for me? What happened to the 
one we picked up on the scanners?!"
''')
            # sleep(4)
            cprint('''
"Still looking my lord. We have not seen it since for several minutes. We did scramble the crew, but many of 
them have given up.
''')
            # sleep(4)
            cprint('''
You realize that something is wrong, but all you can think about is getting to the bridge. You study the Commander 
as he talks to his subordinant.
''')
            option = ''
            # sleep(1)
            while option != '1' and option != '2':
                option = input('''
What would you like to do?
    1. Attempt to sneak past the guard.
    2. Raise your weapon and run in like a crazy person.
''')
            if option == '1':
                # sleep(1)
                cprint('''
You settle your equipment and carefully step out. You see another door 10 feet down the hall on the left side.
''')
                # sleep(1)
                sneak = randint(1, 21)
                if self.player.sneak >= sneak:
                    cprint('''
You slowly put one foot in front of the other and make your way to the second door. You discreetly flash the key
card and re-enter the password. As the door hisses open you see the Commander's head start to turn, but not before
you are able to slam it shut and blast the panel. They won't be following you.
''')
                    # sleep(5)
                    self.player.specialAction2 = False
                    self.player.lookAround4 = True

                else:
                    cprint('''
You slowly put one foot in front of the other and make your way to the second door. After a few steps, the
Commander whips his head around and raises his blaster before you can react. You feel an impossibly hot pain
in your chest as the world goes dark.
''')
                    # sleep(5)
                    self.battle2 = True
                    self.battleTwo()
                    # sleep(1)
                    cprint('''
You finish off the Commander with gusto. He didn't even have a name tag; he had no chance.
''')
                    self.player.specialAction2 = False
                    self.player.lookAround3 = True

            elif option == '2':
                # sleep(1)
                cprint('''
You raise your weapon and scream. Your voice jumps to a higher octave than you expect it to. The grunt standing
next to the Commander screams even higher and runs away.
''')
                # sleep(4)
                cprint('''
The Commander raises his rifle and aims for your chest. You barrel-roll to the right and feel the hot light 
flash inches from your left eye. You raise your weapon...
''')
                # sleep(4)
                self.battle2 = True
                self.battleTwo()
                # sleep(1)
                cprint('''
You finish off the Commander with gusto. He didn't even have a name tag; he had no chance.
''')
                self.player.specialAction2 = False
                self.player.lookAround3 = True

        else:
            cprint('''
You're not sure what to do...
''')

    def scene2UseItem(self):
        """Controls order of all 'use item' actions in scene 2."""
        if self.player.useItem1 == True:
            cprint('''
You locate the security door that leads to a hallway. At the side of the door is a key pad. You swipe the pirate's
key card and a message appears on the screen:
''')
            # sleep(3)
            cprint('''
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
                # sleep(1)
                cprint('''
You easily guess the fool's password and the door slides open with a cool hiss.
''')
            self.player.useItem1 = False
            self.player.specialAction1 = False
            self.player.specialAction2 = True

        else:
            cprint('''
You don't have any items worth using right now.
''')

class sceneThree:
    def __init__(self):
        self.scene3 = False

    def sceneThree(self):
        """Main actions for Scene 1"""
        action = ''
        while action != "1" and action != "2" and action != "3" and action != "4" and action != "5" and action != '6':
            action = input('''
What would you like to do?
1. Look Around.     3. Special Action.      5. Rest.
2. Show Stats.      4. Use Item.            6. Give up.
>>>
''')
        if action == "1":
            # sleep(1)
            self.scene3LookAround()

        if action == "2":
            self.displayStats()
        
        if action == "3":
            # sleep(1)
            self.scene3SpecialAction()

        if action == "4":
            # sleep(1)
            self.scene3UseItem()

        if action == "5":
            # sleep(1)
            self.rest()

        if action == "6":
            confirm = ''
            while confirm != '1' and confirm != '2':
                # sleep(1)
                confirm = input('''
Are you sure you want to give up?
1. Yes
2. No way!
''')
            if confirm == '1':
                # sleep(1)
                self.gameOver()

            elif confirm == '2':
                self.sceneThree()

    def scene3LookAround(self):
        """Controls order of all 'look around' actions in scene 3."""
        if self.player.lookAround1 == False:
            cprint('''
The ship's bridge room is quaint. There aren't a lot of bells and whistles, but you
feel confident enough to pilot this thing home. 
''')
            # sleep(4)
            cprint('''
The room is in complete disarray. Seats are overturned, a dead pirate lays in the corner,
and there are sparks emitting from one of the computers. It is completely silent.
''')
            # sleep(4)
            cprint('''
Where is everybody?
''')
            # sleep(3)
            cprint('''
You see a computer at the center of the room in front of the large viewport.
''')
            self.player.lookAround1 = True
            self.player.useItem1 = True

        elif self.player.lookAround2 == True:
            cprint('''
Oh yeah, the dead guy! You walk over to the dead Baustenian in the corner and rifle through
his pockets. You find another key card and hope it gives you full access.
''')
            self.player.items.append('officer key card')
            # sleep(4)
            cprint('''
As you prepare to leave the man, you feel something ice cold in his pockets. It startles you, but
you investigate further. From his front-right pocket you produce a small, metal sphere.
''')
            # sleep(4)
            cprint('''
It's absolutely without blemish and sits in your hand about 2 inches in diameter. It's impossibly
smooth and feels like it's made of ice. Though it looks as if it could survive a super-nova blast
it weighs no more than a feather.
''')
            # sleep(5)
            cprint('''
Amazed, you take it.
''')
            self.player.items.append('cool ball')
            self.player.lookAround2 = False
            self.player.specialAction1 = True

        elif self.player.lookAround3 == True:
            cprint('''
As you begin entering the coordinates for earth, something out of the corner of your eye flashes,
and you jolt your head up. By now you are an inch away from total insanity.
''')
            # sleep(4)
            cprint('''
Through the dirty glass of the viewport, you see a massive abomination of an object.
''')
            # sleep(3)
            cprint('''
Is it a ship?
''')
            # sleep(2)
            cprint('''
Yes, it is... but there is no logic to its design. Its sharp edge and spikes set it apart 
from any ship you've seen or studied throughout your time in the Corps.
''')
            self.player.lookAround3 = False
            self.player.specialAction2 = True

        else: 
            cprint('''
You have already looked around.
''')

    def scene3SpecialAction(self):
        """Controls order of all 'special actions' in scene 3."""
        if self.player.specialAction1 == True:
            cprint('''
You make your way over to the computer terminal with fresh credentials. You scan them and... 
''')
            # sleep(3)

            randomDeath = randint(1, 10)
            live = randint(1, 10)
            if randomDeath != live:
                cprint('''
Success! The navigational systems display, and it looks like the ship has enough integrity to
make the jump back to earth.
''')        
                self.player.specialAction1 = False
                self.player.lookAround3 = True

            else:
                cprint('''
No! The computer is damaged beyond repair. There is no way to fix it. All hope is lost...
''')
                # sleep(2)
                self.gameOver()
        
        elif self.player.specialAction2 == True:
            cprint('''
As you scramble to finish entering the coordinates and priming the hyperdrive, you now
realize that the Pirates weren't worried about you. The real foe lie ahead of you. Perhaps
they are the ones responsible for destroying your ship.
''')
            # sleep(5)
            cprint('''
Your mind has crossed the line of sanity. You are now screaming. Your panic falls
silent on the empty room; your only audience a corpse.
''')
            # sleep(4)
            cprint('''
The last thing you hear is a subtle clicking noise behind you. You have just enough time to turn
and see a grotesque, scaled creature coiled around a locker on the far side of the room. In the
blink of an eye it crosses the space between you and lurches. Your vision goes dark.
''')
            # sleep(3)
            self.player.specialAction2 = False
            self.scene3 = False
        
        else:
            cprint('''
You're not sure what to do...
''')

    def scene3UseItem(self):
        """Controls order of all 'use item' actions in scene 3."""
        if self.player.useItem1 == True:
            cprint('''
You pull out your pirate key card and hope it works just one more time. You approach
the terminal and insert the card.
''')
            # sleep(3)
            cprint('''
Welcome Grunt Grek.
''')
            # sleep(2)
            cprint('''
The ship displays a few functional options, but you are barred from the navigation and
piloting functions.
''')
            self.player.useItem1 = False
            self.player.lookAround2 = True
        
        else:
            cprint('''
You don't have any items worth using right now.
''')



def battleOne(self):
    """Main actions for Battle 1"""
    while self.battle1 == True:
        self.b1PlayerAttack()
        # sleep(2)
        self.b1CheckHealth()
        # sleep(2)
        if self.battle1 == True:
            # sleep(2)
            self.b1EnemyAttack()
            # sleep(2)
            self.b1CheckHealth()
            # sleep(2)
    # sleep(1)
    cprint('''
You finish off the Bausten Pirate thug, and it looks like no one heard or saw you. You should be sneaky...
''')

def b1PlayerAttack(self):
    """Controls all player attacks in battle 1"""
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
            cprint(f'''
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
                    # sleep(1)
                    cprint('''
You lay down your weapon and the enemy overtakes you...
''')
                    # sleep(1)
                    self.gameOver()

                elif confirm == '2':
                    self.b1PlayerAttack()

def b1CheckHealth(self):
    """Check's health in battle and who is alive."""
    if self.player.currentHp <= 0:
        cprint('''
The enemy takes a swing and hits you square in temple. Your vision goes black, and the
world goes cold...
''')    
        # sleep(1)
        self.gameOver()

    elif self.grek.currentHp <= 0:
        cprint(f'''
You bash {self.grek.name} across the face and he falls lifeless.
''')
        self.battle1 = False

    else:
        self.displayStats()      
    
def b1EnemyAttack(self):
    """Controls all player attacks in battle 1"""
    damage = randint(1, self.grek.power)
    cprint(f'''
{self.grek.name} snarls and swings wildly at you. You take {damage} points
of damage!
''')
    self.player.currentHp -= damage

def battleTwo(self):
    """Main actions for Battle 2"""
    while self.battle2 == True:
        self.b2PlayerAttack()
        # sleep(2)
        self.b2CheckHealth()
        # sleep(1)
        if self.battle2 == True:
            # sleep(1)
            self.b2EnemyAttack()
            # sleep(2)
            self.b2CheckHealth()
            # sleep(1)



def b2PlayerAttack(self):
    """Controls all player attacks in battle 1"""
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
            cprint(f'''
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
                    # sleep(1)
                    cprint('''
You lay down your weapon and the enemy overtakes you...
''')
                    # sleep(1)
                    self.gameOver()

                elif confirm == '2':
                    self.b2PlayerAttack()

def b2EnemyAttack(self):
    """Controls all player attacks in battle 1"""
    damage = randint(1, self.commander.power)
    cprint(f'''
{self.commander.name} snarls and swings wildly at you. You take {damage} points
of damage!
''')
    self.player.currentHp -= damage

def b2CheckHealth(self):
        """Check's health in battle and who is alive."""
        if self.player.currentHp <= 0:
            cprint('''
The enemy takes a swing and hits you square in temple. Your vision goes black, and the
world goes cold...
''')    
            # sleep(1)
            self.gameOver()

        elif self.commander.currentHp <= 0:
            # sleep(1)
            cprint(f'''
You bash {self.commander.name} across the face and he falls lifeless.
''')
            self.battle2 = False

        else:
            self.displayStats()  

# Create instances of classes
plurn = Plurn()
s1 = SceneOne()
s2 = SceneTwo()
s3= sceneThree()

# Start Game
plurn.openingSceneGetName()

# Main Game Loops
########### Scene 1 ###########
while s1.scene1 == True:
    s1.sceneOne()

########### Scene 2 ###########
s2.sceneTwoOpen()
plurn.battleOne()
while s2.scene2 == True:
    s2.sceneTwo()
    

########### Scene 3 ###########
while s3.scene3 == True:
    s3.sceneThree()

# End Game
plurn.closingScene()

