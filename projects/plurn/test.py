class Character:
    def __init__(self, name, title, power, attack):
        self.name = name
        self.title = title
        self.power = power
        self.attack = attack


blake = Character("Blake", "Boss", 11, 14)

print(blake.power)

blake = Character("Lein", "student", 200, 11111)

print(blake.power)
print(blake.name)