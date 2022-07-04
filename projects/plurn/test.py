from cprint import cprint
from colors import Colors as c
from random import randint
from plurnCharacter import Character
from plurn import Plurn

player = Character("Bobby", f"{c.CYAN}P.L.U.R.N. Corps Soldier{c.END}", 6, 1, 22, 3)

def playerAttack(enemy):
    """Controls all player attacks in battle 1"""
    attack = ''
    while attack != '1' and attack != '2' and attack != '3':
        attack = input(f'''
{c.BOLD}{c.ITALIC}{c.RED}Battle!{c.END} What would you like to do?
1. {c.GREEN}Attack{c.END}
# 2. {c.YELLOW}Check Stats{c.END}
2. {c.RED}Drop your weapon and give up...{c.END}
''')
        if attack == '1':
            damage = randint(1, player.power)
            cprint(f'''
{c.ITALIC}{c.DARK_GRAY}You swing your weapon with force at {enemy.name}! You deal {c.RED}{damage} points {c.DARK_GRAY}of damage!{c.END}
''')
            enemy.currentHp -= damage

        while attack == '2':
            Plurn.displayStats()
            break

        while attack == '3':
            confirm = ''
            while confirm != '1' and confirm != '2':
                confirm = input(f'''
{c.ITALIC}{c.DARK_GRAY}Are you...sure...you want to do that?
1. {c.RED}Absolutely
{c.DARK_GRAY}2. {c.RED}Nevermind{c.END}
''')
                if confirm == '1':
    
                    cprint(f'''
{c.ITALIC}{c.DARK_GRAY}You lay down your weapon and the enemy overtakes you...{c.END}
''')
                    Plurn.gameOver()

                elif confirm == '2':
                    attack = ""
                    break


def checkHealth(self, enemy):
    """Check's health in battle and who is alive."""
    if player.currentHp <= 0:
        cprint(f'''
{c.ITALIC}{c.DARK_GRAY}The enemy takes a swing and hits you square in temple. Your vision goes black, and the
world goes cold...{c.END}
''')    
        Plurn.gameOver()

    elif enemy.currentHp <= 0:
        cprint(f'''
You bash {enemy.name} across the face and he falls lifeless.
''')
        Plurn.battleFlag = False

    else:
        Plurn.displayStats()      

def enemyAttack(self, enemy):
    """Controls all player attacks in battle 1"""
    damage = randint(1, enemy.power)
    cprint(f'''
{c.ITALIC}{enemy.name} {c.DARK_GRAY}snarls and swings wildly at you. You take {c.RED}{damage} {c.DARK_GRAY}points
of damage!{c.END}
''')
    player.currentHp -= damage


def battle(self, enemy):
    """Main actions for Battle 1"""
    while Plurn.battleFlag == True:
        playerAttack(enemy)
        checkHealth(enemy)
        if Plurn.battleFlag == True:
            enemyAttack(enemy)
            checkHealth(enemy)
    cprint('''
You finish off the Bausten Pirate thug, and it looks like no one heard or saw you. You should be sneaky...
''')
Plurn.battleFlag = True
battle(Character(f"{c.LIGHT_GREEN}Grek{c.END}", "Grunt", 7, 16, 16, 5))
