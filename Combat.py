from Player import *
from Enemy import *

class Combat:
    def __init__(self):
        pass

    def playerAttack(self, player , enemy):
        print('You deal ' + str(player.strength) + ' damage')
        enemy.hp -= player.strength
        return enemy.hp

    def enemyAttack(self, player, enemy):
        print(enemy.name + ' deals ' + str(enemy.strength) + ' damage')
        player.hp -= enemy.strength
        return player.hp
    
    

