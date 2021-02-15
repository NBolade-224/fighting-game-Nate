from Player import *

class Shop:
    def __init__(self):
        
        self.items = {}
        self.itemNames = []
        
    def printShop(self):
        itemCount = 0
        for name in self.itemNames:
            itemCount+=1
            print(' {})  {} costs {} coins'.format(itemCount, name, self.items[name]))

    def optionToItem(self, option):
      
        name = self.itemNames[option-1]
        return (name, self.items[name])
    
    def addToShop(self, itemName, itemCost):
        self.itemNames.append(itemName)
        self.items[itemName] = itemCost
        
        
    

    
