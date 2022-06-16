from time import sleep
from random import randint
from plurnCharacter import Character
from plurn import Plurn

class BattleOne:
    def __init__(self):
        self.grek = Character("Pirate Grek", 5, 15, 15, 0)
        self.battle1 = True
    
    
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
                damage = randint(1, self.plurn.player.power)
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


class BattleTwo:
    pass