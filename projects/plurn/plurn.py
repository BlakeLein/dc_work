# Import Special Functions
import sys
from random import randint
from time import sleep
from cprint import cprint


# Import Other Game Modules
from plurnCharacter import Character
from colors import Colors as c


class Plurn:
    """Main class for Plurn 1"""
    def __init__(self):
        self.player = Character("name", "person", 1, 1, 1, 1)
        
        # Variables to control scenes
        self.scene1 = True
        self.scene2 = False
        self.scene3 = False
        self.battleFlag = False

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
    || NAME: {c.BLUE}{self.player.name}{c.END} |||| RANK: {self.player.rank} ||

    <<Hit Points>>
        {c.RED}{self.player.currentHp} / {self.player.maxHp}{c.END}''')
        print('''
    <<Items>>''')                                   
        for i in self.player.items:
            print(f'{c.GREEN}        {i.title()}{c.END}')
        print('''
    <<Equipment>>''')
        for e in self.player.equipment:
            print(f'{c.PURPLE}        {e.title()}{c.END}')

    def rest(self):
        """Heal player if health below max"""
        if self.player.currentHp < self.player.maxHp:
            cprint('''
You find a dark corner and sit for a while. You assess your wounds and do what
you can to patch yourself up.
''')
            self.player.currentHp = self.player.maxHp

        else:     
            cprint(f'''
{c.ITALIC}{c.DARK_GRAY}You don't need to rest.{c.END}
''')

    def gameOver(self):
        """End the game."""
        cprint(f"{c.ITALIC}{c.DARK_GRAY}Game Over.{c.END}")
        cprint(f"{c.ITALIC}{c.DARK_GRAY}You lose.{c.END}")
        sys.exit()

    def openingSceneGetName(self):
        """Opening narrative, get name, and get class"""
        
        cprint(f'{c.ITALIC}{c.DARK_GRAY}Welcome to Plurn. Developed in June 2022 by Blake Lein. (Press Enter)')
        cprint('Please make sure your terminal is in full screen mode.')
        cprint(f'Advance the game with the enter button.{c.END}')
        print(f'{c.BLUE}*******************************************************************************{c.END}')
        cprint('Your eyes slowly open.')
        cprint('You are weightless in a small capsule floating in space.')
        cprint('A light flashes.')
        cprint('There is a faint glow from the local sun.')
        
        cprint(f'{c.ITALIC}{c.DARK_GRAY}Do you remember your name? (Press Enter, then type in your name){c.END}')
        self.player.name = input(f'''
{c.DARK_GRAY}>>>{c.END} ''').title()

        cprint(f'Yes, you remember. Your name is {c.BLUE}{self.player.name}{c.END}.')
        cprint('You are a member of the P.L.U.R.N. Space Corps.')
        rank = ''
        while rank != '1' and rank != '2' and rank != '3':
            print('Do you remember your rank? (Press Enter, then choose a rank)')
            rank = input(f'''
    1. {c.CYAN}Soldier (+ Attack, + Health, - Sneak){c.END}
    2. {c.YELLOW}Operative (+ Attack, - Health, + Sneak){c.END}
    3. {c.RED}Medic (- Attack, + Health, + Sneak){c.END}
>>>
''')
        if rank == '1':
            self.player = Character(f"{self.player.name}", f"{c.CYAN}P.L.U.R.N. Corps Soldier{c.END}", 6, 1, 22, 3)

        elif rank == '2':
            self.player = Character(f"{self.player.name}", f"{c.YELLOW}P.L.U.R.N. Corps Operative{c.END}", 6, 1, 15, 10)

        elif rank == '3':
            self.player = Character(f"{self.player.name}", f"{c.RED}P.L.U.R.N. Corps Medic{c.END}", 4, 1, 25, 10)

    def closingScene(self):
        """Final narration"""
        cprint(f'{c.ITALIC}{c.FAINT}.....')
        cprint('.....')
        cprint('''
Your eyes open. You are badly injured.
''')
        cprint('.....')
        cprint('.....')
        cprint('''
You are in your base clothes and bound by an organic substance in a dark room. You 
guess you are aboard the alien ship.
''')
        cprint('.....')
        cprint('.....')
        cprint('''
You are tired and all out of hope. You no longer fear death.
''')
        cprint('.....')
        cprint('.....')
        cprint('''
You slowly close your eyes and feel yourself slipping back into a deep sleep. As your body
slowly goes limp, you feel nothing but despair...
''')
        cprint('.....')
        cprint('.....')
        cprint('''
...and the icy presence of a metal sphere.
''')
        
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
            self.scene1LookAround()

        if action == "2":
            self.displayStats()
        
        if action == "3":
            self.scene1SpecialAction()

        if action == "4":
            self.scene1UseItem()

        if action == "5":
            self.rest()
        
        if action == "6":
            confirm = ''
            while confirm != '1' and confirm != '2':
                confirm = input(f'''
{c.ITALIC}{c.DARK_GRAY}Are you sure you want to give up?
1. {c.RED}Yes
{c.DARK_GRAY}2. {c.GREEN}No way! Keep Playing!{c.END}
''')
            if confirm == '1':

                self.gameOver()

            elif confirm == '2':

                self.sceneOne()

    def scene1LookAround(self):
        """Controls order of all 'look around' actions in scene 1."""
        if self.lookAround1 == False:
            cprint('''
You feel your way around the dark capsule. It looks like an an escape pod. By the looks of the 
registration number and P.L.U.R.N. Space Corps crest, you know you are in an escape pod for
your ship - the 'Plurning Star.'
''')
            cprint('''
You clamber over to the viewport and see a field of debris amongst the stars. As some pieces of rubble 
float across your capsule, you recognize the twisted metal as the meager remnants of your ship.
''')
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

            cprint('''
It's filthy and unkept, and on the sides above the rear thrusters, you see the blood-red sun surrounded 
by black flames. You recognize this as the logo of the Bausten Pirate Syndicate.
''')
            self.lookAround2 = False
            self.specialAction1 = True

        elif self.lookAround3 == True:
            cprint('''
You decide to take another glance around the pod with the lights back on. You find a pair of shoes that
look more comfortable than the ones you have on. You decide to put them on.
''')
            self.player.equipment.append("soft shoes")
            self.player.sneak += 5

            cprint('''
As you turn to your right, you see her lifeless body strapped to a seat. Pam. You've known her since you
both joined up, and now she's gone while you keep going.
''')
            cprint('''
She managed to don a kevlar space vest during the evacuation sequence. You have to press forward, and you 
may need that vest if pirates are involved.
''')
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
            cprint('''
Then you see it again. The Pirate ship is floating slowly aross your view, and you notice the docking bay is
wide open. If you could time it perfectly, you could use what fuel remains in the pod to jetison into
the docking bay of the other ship.
''')
            cprint('''
You quickly make your way to the console and initialize the engine thrust sequence. You only have one shot.
''')
            guess = 0
            while guess > 5 or guess < 1:
                try:
                    guess = int(input(f'''
{c.ITALIC}{c.DARK_GRAY}(Pick a number between 1 and 5){c.END}
'''))
                except ValueError:
                    cprint(f'{c.DARK_GRAY}Please type a number.{c.END}')
            failure = randint(1, 5)
            if guess == failure:

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

                cprint('''
As the shuttle begins to rapidly spin, it makes it into the bay and slams into a panel on the wall. 
The docking bay doors slam shut and the ship's artificial gravity takes hold. You fall to the floor and 
the air is knocked from your lungs. Over the sound of oxygen rushing into the docking bay, you hear
a pirate running toward your ship...
''')

                cprint(f'''
{c.ITALIC}Now for the next problem...{c.END}
''')

                self.scene2 = True
                self.resetFlags()
                self.battleFlag = True
                self.scene1 = False

        else: 
            cprint(f'''
{c.ITALIC}{c.DARK_GRAY}You have already looked around the capsule.{c.END}
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
            cprint(f'''
{c.BOLD}{c.ITALIC}The Riddle Matrix! Of course!{c.END}
''')
            cprint('''
You locate the matrix symbol at the bottom-right of the screen. The stakes couldn't be higher, but
the circumstances couldn't be more dire. You click the symbol, and the screen goes black.
''')
            
            cprint(f'''
    {c.ITALIC}{c.DARK_GRAY}Welcome to Plurn: The Riddles of Queelix! I will ask of you a riddle, and your answer will determine your fate.
    ''')
            cprint(f'''
    {c.ITALIC}{c.DARK_GRAY}You are walking down a path on your way to a funeral. You come up to an intersection where a goblin lay against
    the sign post. "Please traveler" the goblin rasps. "Help me cure my wounds so I may return to my family."
    ''')
            choice = ''
            while choice != "1" and choice != "2":
                choice = input(f'''
    What do you you do?
    1. {c.GREEN}Help Goblin. He just wants to see his children again.
    {c.ITALIC}{c.DARK_GRAY}2. {c.RED}Shoot Goblin.{c.END}
    ''')
                if choice == "1":
    
                    cprint(f'''
    {c.ITALIC}{c.DARK_GRAY}As you bend over to offer the goblin a helping hand, several more goblins spring forth and stab you to death.
    You were a fool to believe a goblin would ask you for help.{c.END}
    ''')
    
                    cprint(f'''
{c.ITALIC}{c.BOLD}{c.RED}RIDDLE MATRIX DETECTS INTRUDER. SYSTEM ALERT. IMMEDIATE SELF-DESTRUCT SEQUENCE INITIALIZED.{c.END}
''')
    
                    self.gameOver()

                elif choice == "2":
    
                    cprint(f'''
    {c.ITALIC}{c.DARK_GRAY}Almost before the goblin can finish asking for help, you take your crossbow and give him one between
    the eyes. Everyone knows that goblins hate humans. Several other goblins scatter in a frenzied panic. You
    go ahead and shoot them too.{c.END}
''')
    
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
                choice2 = input(f'''
    {c.ITALIC}{c.DARK_GRAY}What option do you select?
        1. Escape Pod Diagnostics
        2. Escape Pod Logs
        3. Escape Pod Functions{c.END}
    ''')
                if choice2 == "1":
    
                    cprint(f'''
    OCCUPANTS: {c.DARK_GRAY}2{c.END}
    OXYGEN LEVELS: {c.RED}8%{c.END}
    LIFE SUPPORT STATUS: {c.GREEN}Stable{c.END}
    FUEL LEVEL: {c.RED}5%{c.END}
    MANEUVERABILITY: {c.DARK_GRAY}Disabled{c.END}
    HYDERDRIVE: {c.DARK_GRAY}Decomissioned{c.END}
    SIGNAL TO PLURNING STAR: {c.DARK_GRAY}---{c.END}
    ''')
                if choice2 == "2":
    
                    cprint(f'''
    {c.DARK_GRAY}NO LOGS TO DISPLAY.{c.END}
    ''')
                if choice2 == "3":
    
                    cprint(f'''
    {c.ITALIC}{c.DARK_GRAY}ESCAPE POD FUNCTIONS:
    - Self Destruct
    - Engine Thrust
    - Jetison Fuel{c.END}
    ''')
                    
    
                    cprint('''
You realize the escape pod has no way to steer. Other than a quick rear-engine thrust that will
launch you forward, you are dead in the water...
''')
                    proceed = 'y'
                    self.specialAction2 = False
                    self.lookAround4 = True

        else:
            cprint(f'''
{c.ITALIC}{c.DARK_GRAY}You're not sure what to do...{c.END}
''')

    def scene1UseItem(self):
        """Controls order of all 'usse item' actions in scene 1."""
        if self.useItem1 == True:                
            cprint('''
You float over to the computer and take a closer look. After about 10 minutes of recalling 
your space training and trying not to electrocute yourself, you manage to reattach the power
cell. The computer comes to life and the glow of the monitor stings your eyes.
''')

            cprint('''
The computer displays the P.L.U.R.N. Space Corps logo along with the taunting motto - 
"A safer world for all mankind." Some motto. You see a login menu for a P.L.U.R.N. Officer to
sign in. You don't have such credentials. The only way in is by force.
''')
            self.player.items.remove('power cell')
            self.useItem1 = False
            self.lookAround2 = True

        else:
            cprint(f'''
{c.ITALIC}{c.DARK_GRAY}You don't have any items worth using right now.{c.END}
''')

    def sceneTwoOpen(self):
        """Transitions from Scene 1 to Scene 2"""
        cprint('''
You get to your feet in time to see a hulking Bausten Pirate burst through the door with an electro-baton
crackling. You grab your metal pipe and charge!
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
            self.scene2LookAround()

        if action == "2":
            self.displayStats()
        
        if action == "3":
            self.scene2SpecialAction()

        if action == "4":
            self.scene2UseItem()

        if action == "5":
            self.rest()
        
        if action == "6":
            confirm = ''
            while confirm != '1' and confirm != '2':
                confirm = input(f'''
{c.ITALIC}{c.DARK_GRAY}Are you sure you want to give up?
1. {c.RED}Yes
{c.DARK_GRAY}2. {c.GREEN}No way! Keep Playing!{c.END}
''')
            if confirm == '1':

                self.gameOver()

            elif confirm == '2':
                self.sceneTwo()

    def scene2LookAround(self):
        """Controls order of all 'look around' actions in scene 2."""
        if self.lookAround1 == False:
            cprint('''
You walk over to the pirate and check his pulse. Dead. You notice his weapon was badly damaged
in the battle. You do notice a key card in his satchel, and decide to take that...
''')
            self.player.items.append("pirate key card")
            cprint('''
Now that you think of it, the pirate is generally the same size as you. You think it might be a good
idea to put on his clothes...maybe it will be a nice disguise?
''')
            disguise = ''
            while disguise != '1' and disguise != '2':
                disguise = input(f'''
{c.ITALIC}{c.DARK_GRAY}Do you put on the pirate's outfit?
    1. {c.GREEN}Yeah, duh.
    {c.ITALIC}{c.DARK_GRAY}2. {c.RED}No, that's gross.{c.END}
''')
            if disguise == '1':
                cprint('''
You take a couple minutes to put on the pirate's clothes and practice your best pirate voice. You've got this.
''')
                caught = randint(1, 5)
                if caught == 3:
    
                    cprint('''
As you are putting on the smelly garb, another pirate comes up behind you and clubs you on the head. Why
did you think it was a good idea to change outfits in the middle of an enemy ship?
''')
    
                    self.gameOver()
                
                else:
                    cprint('''
You successfully put on the pirate's clothes, and you look terrible! Perfect! Maybe this will
fool any other pirates you come across.
''')
    
                    self.player.equipment.append('pirate clothes')
                    self.player.sneak += 5
            
            elif disguise == '2':
                cprint('''
Why would you put on a discguise in the middle of an enemy ship? You carefully drag the pirate's body behind
a crate in a dark corner and leave him.
''')

            self.lookAround1 = True
            self.lookAround2 = True
        
        elif self.lookAround2 == True:
            cprint('''
You take a moment to survey the situation. You are standing alone in a docking bay with a destroyed ship in
one corner and a dead pirate in the other corner. For some strange reason, no one has come running to the
bay as a result of an escape pod crashing into it...
''')
            cprint('''
You know that a ship this size has a hyperdrive. Maybe you can get to the bridge, seal yourself in, and make
the jump to earth. From there you could fly to Plurnquarters and help bring these pirates to justice.
''')
            self.lookAround2 = False
            self.specialAction1 = True
            self.useItem1 = True

        elif self.lookAround3 == True:
            cprint('''
You notice the Commander has a really neat helmet. Man that helmet looks neat. Mine!
''')
            self.player.equipment.append('pirate helmet')
            self.player.currentHp += 5
            self.player.maxHp += 5
            self.lookAround3 = False
            self.lookAround4 = True

            cprint('''
You step over the Commander's helmetless corpse and make your way to another security door in the hallway.
You flash your key card and it snaps open.
''')

        elif self.lookAround4 == True:
            cprint('''
You are standing in a small room with another door right in front of you. Based on your feel for the 
layout of this vessel, you know that you are looking at the door to the bridge...
''')
            cprint('''
Almost home.
''')
            cprint('''
It's so quiet. You no longer hear the hustle and bustle of pirates scrambling to find you. Were they looking
for you? Or someone else?
''')

            cprint('''
You ready yourself with weapon drawn and creep toward the door.
''')
            self.scene3 = True
            self.resetFlags()
            self.scene2 = False

        else: 
            cprint(f'''
{c.ITALIC}{c.DARK_GRAY}You have already looked around.{c.END}
''')

    def scene2SpecialAction(self):
        """Controls order of all 'special actions' in scene 2."""
        if self.specialAction1 == True:
            cprint('''
You look into the crate obscurring the dead pirate and find a few blaster rifles. You have never been more elated
in your entire life. You grab one and throw the metal pipe across the room.
''')
            self.player.equipment.remove('metal pipe')
            self.player.equipment.append('blaster rifle')
            self.player.power += 3
            self.specialAction1 = False

        elif self.specialAction2 == True:
            cprint('''
You poke your head through the now open door and swipe it side to side. On your left is a dead-end. On your right 
is a man standing a head taller than the average man with a large gun strapped to his back. He is talking to another
and you hear him referred to as 'Commander.'
''')
            cprint('''
So this is the one in charge. The one you have to worry about. You slink back and listen to them talk.
''')
            cprint('''
"The wreckage was here when we arrived my Lord. We picked up the debris and figured we could be the first to scavenge.
We didn't expect- "
''')
            cprint('''
"Of course you didn't expect them fool! Do you have any meaningful updates for me? What happened to the 
one we picked up on the scanners?!"
''')
            cprint('''
"Still looking my lord. We have not seen it since for several minutes. We did scramble the crew, but many of 
them have given up.
''')
            cprint('''
You realize that something is wrong, but all you can think about is getting to the bridge. You study the Commander 
as he talks to his subordinant.
''')
            option = ''
            while option != '1' and option != '2':
                option = input(f'''
{c.ITALIC}{c.DARK_GRAY}What would you like to do?
    1. {c.GREEN}Attempt to sneak past the guard.
    {c.ITALIC}{c.DARK_GRAY}2. {c.RED}Raise your weapon and run in like a crazy person.{c.END}
''')
            if option == '1':

                cprint('''
You settle your equipment and carefully step out. You see another door 10 feet down the hall on the left side.
''')

                sneak = randint(1, 21)
                if self.player.sneak >= sneak:
                    cprint('''
You slowly put one foot in front of the other and make your way to the second door. You discreetly flash the key
card and re-enter the password. As the door hisses open you see the Commander's head start to turn, but not before
you are able to slam it shut and blast the panel. They won't be following you.
''')
    
                    self.specialAction2 = False
                    self.lookAround4 = True

                else:
                    cprint('''
You slowly put one foot in front of the other and make your way to the second door. After a few steps, the
Commander whips his head around and raises his blaster before you can react. You feel an impossibly hot pain
in your chest as the world goes dark.
''')
    
                    self.battleFlag = True
                    self.battle(Character(f"{c.LIGHT_RED}Commander Matthew{c.END}", "Commander", 10, 20, 20, 100))
    
                    cprint('''
You finish off the Commander with gusto. He didn't even have a name tag; he had no chance.
''')

                    self.specialAction2 = False
                    self.lookAround3 = True

            elif option == '2':

                cprint('''
You raise your weapon and scream. Your voice jumps to a higher octave than you expect it to. The grunt standing
next to the Commander screams even higher and runs away.
''')

                cprint('''
The Commander raises his rifle and aims for your chest. You barrel-roll to the right and feel the hot light 
flash inches from your left eye. You raise your weapon...
''')

                self.battleFlag = True
                self.battle(Character(f"{c.LIGHT_RED}Commander Matthew{c.END}", "Commander", 10, 20, 20, 100))

                cprint('''
You finish off the Commander with gusto. He didn't even have a name tag; he had no chance.
''')
                self.specialAction2 = False
                self.lookAround3 = True

        else:
            cprint(f'''
{c.ITALIC}{c.DARK_GRAY}You're not sure what to do...{c.END}
''')

    def scene2UseItem(self):
        """Controls order of all 'use item' actions in scene 2."""
        if self.useItem1 == True:
            cprint('''
You locate the security door that leads to a hallway. At the side of the door is a key pad. You swipe the pirate's
key card and a message appears on the screen:
''')
            cprint(f'''
        USER: {c.YELLOW}Grek{c.END}
        RANK: {c.DARK_GRAY}Grunt{c.END}
        RATING: {c.RED}3 / 10{c.END}
        
        To proceed, please enter your password:
''')

            hack = ''
            while hack != '1' and hack != '2':
                hack = input(f'''
            {c.ITALIC}{c.DARK_GRAY}1. You type in 'password'
            2. You type in '12345'{c.END}
''')
            if hack == '1' or hack == '2':

                cprint('''
You easily guess the fool's password and the door slides open with a cool hiss.
''')
            self.useItem1 = False
            self.specialAction1 = False
            self.specialAction2 = True

        else:
            cprint(f'''
{c.ITALIC}{c.DARK_GRAY}You don't have any items worth using right now.{c.END}
''')

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
            self.scene3LookAround()

        if action == "2":
            self.displayStats()
        
        if action == "3":
            self.scene3SpecialAction()

        if action == "4":
            self.scene3UseItem()

        if action == "5":
            self.rest()

        if action == "6":
            confirm = ''
            while confirm != '1' and confirm != '2':

                confirm = input(f'''
{c.ITALIC}{c.DARK_GRAY}Are you sure you want to give up?
1. {c.RED}Yes
{c.DARK_GRAY}2. {c.GREEN}No way! Keep Playing!{c.END}
''')
            if confirm == '1':

                self.gameOver()

            elif confirm == '2':
                self.sceneThree()

    def scene3LookAround(self):
        """Controls order of all 'look around' actions in scene 3."""
        if self.lookAround1 == False:
            cprint('''
The ship's bridge room is quaint. There aren't a lot of bells and whistles, but you
feel confident enough to pilot this thing home. 
''')
            cprint('''
The room is in complete disarray. Seats are overturned, a dead pirate lays in the corner,
and there are sparks emitting from one of the computers. It is completely silent.
''')
            cprint('''
Where is everybody?
''')
            cprint('''
You see a computer at the center of the room in front of the large viewport.
''')
            self.lookAround1 = True
            self.useItem1 = True

        elif self.lookAround2 == True:
            cprint('''
Oh yeah, the dead guy! You walk over to the dead Baustenian in the corner and rifle through
his pockets. You find another key card and hope it gives you full access.
''')
            self.player.items.append('officer key card')
            cprint('''
As you prepare to leave the man, you feel something ice cold in his pockets. It startles you, but
you investigate further. From his front-right pocket you produce a small, metal sphere.
''')
            cprint(f'''
{c.ITALIC}It's absolutely without blemish and sits in your hand about 2 inches in diameter. It's impossibly
smooth and feels like it's made of ice. Though it looks as if it could survive a super-nova blast
it weighs no more than a feather.{c.END}
''')
            cprint('''
Amazed, you take it.
''')
            self.player.items.append('cool ball')
            self.lookAround2 = False
            self.specialAction1 = True

        elif self.lookAround3 == True:
            cprint('''
As you begin entering the coordinates for earth, something out of the corner of your eye flashes,
and you jolt your head up. By now you are an inch away from total insanity.
''')
            cprint('''
Through the dirty glass of the viewport, you see a massive abomination of an object.
''')
            cprint('''
Is it a ship?
''')
            cprint('''
Yes, it is... but there is no logic to its design. Its sharp edge and spikes set it apart 
from any ship you've seen or studied throughout your time in the Corps.
''')
            self.lookAround3 = False
            self.specialAction2 = True

        else: 
            cprint(f'''
{c.ITALIC}{c.DARK_GRAY}You have already looked around.{c.END}
''')

    def scene3SpecialAction(self):
        """Controls order of all 'special actions' in scene 3."""
        if self.specialAction1 == True:
            cprint('''
You make your way over to the computer terminal with fresh credentials. You scan them and... 
''')

            randomDeath = randint(1, 10)
            live = randint(1, 10)
            if randomDeath != live:
                cprint(f'''
{c.ITALIC}Success!{c.END} The navigational systems display, and it looks like the ship has enough integrity to
make the jump back to earth.
''')        
                self.specialAction1 = False
                self.lookAround3 = True

            else:
                cprint(f'''
{c.ITALIC}No!{c.END} The computer is damaged beyond repair. There is no way to fix it. All hope is lost...
''')

                self.gameOver()
        
        elif self.specialAction2 == True:
            cprint('''
As you scramble to finish entering the coordinates and priming the hyperdrive, you now
realize that the Pirates weren't worried about you. The real foe lie ahead of you. Perhaps
they are the ones responsible for destroying your ship.
''')
            cprint('''
Your mind has crossed the line of sanity. You are now screaming. Your panic falls
silent on the empty room; your only audience a corpse.
''')
            cprint('''
The last thing you hear is a subtle clicking noise behind you. You have just enough time to turn
and see a grotesque, scaled creature coiled around a locker on the far side of the room. In the
blink of an eye it crosses the space between you and lurches. Your vision goes dark.
''')
            self.specialAction2 = False
            self.scene3 = False
        
        else:
            cprint(f'''
{c.ITALIC}{c.DARK_GRAY}You're not sure what to do...{c.END}
''')

    def scene3UseItem(self):
        """Controls order of all 'use item' actions in scene 3."""
        if self.useItem1 == True:
            cprint('''
You pull out your pirate key card and hope it works just one more time. You approach
the terminal and insert the card.
''')
            cprint(f'''
{c.ITALIC}{c.DARK_GRAY}Welcome Grunt Grek.{c.END}
''')
            cprint('''
The ship displays a few functional options, but you are barred from the navigation and
piloting functions.
''')
            self.useItem1 = False
            self.lookAround2 = True
        
        else:
            cprint(f'''
{c.ITALIC}{c.DARK_GRAY}You don't have any items worth using right now.{c.END}
''')

    def battle(self, enemy):
        """Main actions for Battle 1"""
        while self.battleFlag == True:
            self.playerAttack(enemy)
            self.checkHealth(enemy)
            if self.battleFlag == True:
                self.enemyAttack(enemy)
                self.checkHealth(enemy)
        cprint('''
You finish off the Bausten Pirate thug, and it looks like no one heard or saw you. You should be sneaky...
''')

    def playerAttack(self, enemy):
        """Controls all player attacks in battle 1"""
        attack = ''
        while attack != '1' and attack != '2' and attack != '3':
            attack = input(f'''
{c.BOLD}{c.ITALIC}{c.RED}Battle!{c.END} What would you like to do?
1. {c.GREEN}Attack{c.END}
2. {c.YELLOW}Check Stats{c.END}
3. {c.RED}Drop your weapon and give up...{c.END}
''')
            if attack == '1':
                damage = randint(1, self.player.power)
                cprint(f'''
{c.ITALIC}{c.DARK_GRAY}You swing your weapon with force at {enemy.name}! You deal {c.RED}{damage} points {c.DARK_GRAY}of damage!{c.END}
''')
                enemy.currentHp -= damage

            if attack == '2':
                self.displayStats()
                self.playerAttack(enemy)

            if attack == '3':
                confirm = ''
                while confirm != '1' and confirm != '2':
                    confirm = input(f'''
{c.ITALIC}{c.DARK_GRAY}Are you...sure...you want to do that?
1. {c.RED}Absolutely
{c.DARK_GRAY}2. {c.GREEN}Nevermind{c.END}
''')
                    if confirm == '1':
        
                        cprint(f'''
{c.ITALIC}{c.DARK_GRAY}You lay down your weapon and the enemy overtakes you...{c.END}
''')
                        self.gameOver()

                    elif confirm == '2':
                        self.playerAttack(enemy)


    def checkHealth(self, enemy):
        """Check's health in battle and who is alive."""
        if self.player.currentHp <= 0:
            cprint(f'''
{c.ITALIC}{c.DARK_GRAY}The enemy takes a swing and hits you square in temple. Your vision goes black, and the
world goes cold...{c.END}
''')    
            self.gameOver()

        elif enemy.currentHp <= 0:
            cprint(f'''
You bash {enemy.name} across the face and he falls lifeless.
''')
            self.battleFlag = False

        else:
            self.displayStats()      
    
    def enemyAttack(self, enemy):
        """Controls all player attacks in battle 1"""
        damage = randint(1, enemy.power)
        cprint(f'''
{c.ITALIC}{enemy.name} {c.DARK_GRAY}snarls and swings wildly at you. You take {c.RED}{damage} {c.DARK_GRAY}points
of damage!{c.END}
''')
        self.player.currentHp -= damage


# # Create instances of classes
plurn = Plurn()

# Start Game
plurn.openingSceneGetName()

# Main Game Loops
########### Scene 1 ###########
while plurn.scene1 == True:
    plurn.sceneOne()

########## Scene 2 ###########
plurn.sceneTwoOpen()
plurn.battle(Character(f"{c.LIGHT_GREEN}Grek{c.END}", "Grunt", 7, 16, 16, 5))

while plurn.scene2 == True:
    plurn.sceneTwo()

########### Scene 3 ###########
while plurn.scene3 == True:
    plurn.sceneThree()

# End Game
plurn.closingScene()

