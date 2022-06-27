class Character:
    def __init__(self, name="", rank = 'person', power=0, currentHp=0, maxHp=0, sneak=0):
        self.name = name
        self.rank = rank
        self.power = power
        self.currentHp = currentHp
        self.maxHp = maxHp
        self.sneak = sneak
        self.items = []
        self.equipment = []

