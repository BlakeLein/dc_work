class Homer:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    
    def catchPhrase(self):
        print("D'oh!")
    

class Bart(Homer):
    def __init__(self, name, job, school, hobby):
        super().__init__(name, job)
        self.school = school
        self.hobby = hobby

class Lisa(Bart):
    def __init__(self, name, job, school, hobby):
        super().__init__(name, job, school, hobby)
    


homer = Homer("Homer Simpson", "Safety Inspector")

bart = Bart("Bart Simpson", "Trouble Maker", "Springfield Elementary", "Skateboarding")

lisa = Lisa("Lisa Simpson", "Good Student", "Springfield Elementary", "Saxophone")


print(bart.name)
print(lisa.hobby)
