from Combat import *
from Shop import  *
from Enemy import *
from tkinter import *
import random

class Player:
    def __init__(self, hp = 100, strength = 10, healRate = 10, boostRate = 10, playerCoins = 0):
        self.hp = hp
        self.strength = strength
        self.healRate = healRate
        self.boostRate = boostRate
        self.playerCoins = playerCoins
        self.inventory = []


    def heal(self):
        print('You heal ' + player.healRate + ' hp')
        self.hp += self.healRate
        return self.hp

    #def options(self, combat):

    def boost(self):
        self.strength += self.boostRate
        return self.strength
    

    def displayStats(self):
        print('\t[Player Stats]')
        print('\tHealth: {} '.format(self.hp))
        print('\tStrength: {} \n'.format(self.strength))

    def resetStats(self):
        self.hp = 100
        self.strength = 10
    
    def checkHp(self):
        if self.hp < 1:
            print('You died :(')
    
    def displayDeath(self):
        print('you died :(')

    def displayInventory(self):
        print('INVENTORY')
        for x in self.inventory:
            print(x, end=' ')
        print()

    def awardCoins(self):
        award = random.randint(30,50)
        self.playerCoins += award
        print('YOU WON {} COINS\n'.format(award))

    def useItem(self, choice):
        itemName = self.inventory[choice]
        if 'Health' in itemName:
            hpRestore = 30
            self.hp += hpRestore
            print(' you used {} and restored {} hp'.format(itemName, hpRestore))
        if 'Boost' in itemName:
            strengthBoost = 30
            self.strength += strengthBoost
            print('you used {}  and boosted {} attack'.format(itemName, strengthBoost))
        self.inventory.pop(choice)
        return itemName
        
    

       # for attr, value in self.__dict__.items():
          #  print(attr, value)
        









    
        