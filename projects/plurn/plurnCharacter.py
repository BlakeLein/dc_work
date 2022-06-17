class Character:
    def __init__(self, name="", rank = 'person', power=0, currentHp=0, maxHp=0, sneak=0, items=[], equipment=[]):
        self.name = name
        self.power = power
        self.currentHp = currentHp
        self.maxHp = maxHp
        self.sneak = sneak
        self.items = items
        self.equipment = equipment
        self.rank = rank
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