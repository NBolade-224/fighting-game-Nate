class Enemy:
    def __init__(self, name = 'monster', hp = 100, strength = 10, healRate = 10, boostRate = 10):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.healRate = healRate
        self.boostRate = boostRate

    def heal(self):
        print('{} heals {} hp'.format(self.name, self.healRate))
        self.hp += self.healRate
        return self.hp
        

    def displayStats(self):
        print('\t[{} Stats]'.format(self.name))
        print('\tHealth: {} '.format(self.hp))
        print('\tStrength: {} \n'.format(self.strength))
   
    def checkHp(self):
        if self.hp < 1:
            print('The {} died'.format(self.name))

    def enemyIntro(self):
        print('A {} approaches...\n'.format(self.name))
        