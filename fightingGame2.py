from Player import *
from Enemy import *
from Combat import *
from Shop import *
# import pygame
import random
import time

turnCounter = 0
RoundCounter = 1


#player move options
def playerOptions():
    move = ''
    while move != '1' and move != '2' and move !='3':
        print('Choose your move {1 = attack | 2 = heal | 3 = boost | 4 = Inventory}')
        move = input()
        if move == '1':
            combat.playerAttack(player, enemyCounter)
        if move == '2':
            player.heal()
        if move == '3':
            if player.strength >= 30:
                print('Your strength is too high')
                move = ''
            else:
                player.boost()
        if move == '4':
            if len(player.inventory) == 0:
                print('Empty inventory')
                move = ''
            else:
                choice = displayInventory()
                itemName = player.useItem(choice)
                if 'Spear' in itemName:
                    spearDamage = 40
                    print('You use a {} and deal {} damage'.format(itemName, spearDamage))
                    enemy.hp -= arrowDamage
                break

def enemyOptions():
    option = random.randint(1,2)
    if option == 1:
        combat.enemyAttack(player, enemyCounter)
    if option == 2:
        enemies[i].heal()

def displayShop():
    viewShop = ''
    while viewShop != '1' and viewShop !='2':
        print('Would you like to view the shop? { 1 = yes | 2 = no }')
        viewShop = input()
        print()
        if viewShop == '1':
            shop.printShop()
            print('You have ' + str(player.playerCoins) + ' coins')
            shopPurchase()
            print()
        if viewShop == '2':
            print('You exit the shop')
            print()

def displayInventory():
    print('Inventory: ')
    for i, item in enumerate(player.inventory):
        print('{}) {}'.format(i+1, item))
    print('choose an item')
    choice = '0'
    
    
    while int(choice) < 1 or int(choice) > len(player.inventory):
        choice = input()
        if str.isdigit(choice):
            if int(choice) > 0 and int(choice) <= len(player.inventory):
                return int(choice)-1
    


#allows player to buy shop upgrades
def shopPurchase():
    purchase = ''
    #checks if the player has enough coins to buy anything
    if player.playerCoins >= 10:
        while purchase != 'e' and purchase != '1' and purchase != '2' and purchase != '3':
            print('What would you like to buy?')
            print('e = exit')
            purchase = input()
            print()
            
            if purchase == 'e':
                print('You exit the shop...')
                print()
                break
           
            
            shopItem = shop.optionToItem(int(purchase))
            if player.playerCoins < shopItem[1]:
                print('Not enough coins...')
                purchase = ''
            else:
                print('You buy a ' + shopItem[0])
                player.playerCoins -= shopItem[1]
                player.inventory.append(shopItem[0])
                print('You now have ' + str(player.playerCoins) + ' coins')
                purchase = ''
                print()
    else:
        print('you dont have enough coins... exiting shop...')
        


combat = Combat()
shop = Shop()
shop.addToShop('{Health potion}', 10 )
shop.addToShop('{Boost potion}', 10 )
shop.addToShop('{Spear}', 20 )



player = Player(hp = 100, strength=10, healRate=10, boostRate=10, playerCoins =0)
player.inventory =[]




enemy1 = Enemy(name='Goblin Welp', hp=80, strength=10, healRate=10, boostRate=10)
enemy2 = Enemy(name='hitler', hp=50, strength=10, healRate=10, boostRate=10)
enemy3 = Enemy(name='dragon', hp=50, strength=10, healRate=10, boostRate=10)
boss1 = Enemy(name='Volkar', hp=500, strength=20, healRate=10, boostRate=10)
boss2 = Enemy(name='Tribane', hp=250, strength=40, healRate=10, boostRate=10)
boss3 = Enemy(name='Valmeer', hp=250, strength=40, healRate=10, boostRate=10)
enemies = [enemy1, enemy2, enemy3]





i = 0

enemies[i].enemyIntro()
#This loop increments through all the enemy objects until they are all dead
while i < len(enemies):   
    while player.hp > 0 and enemies[i].hp > 0:
        
        #keeps track of turns
        turnCounter += 1
        print('\tTurn: ' + str(turnCounter) +'  Floor: ' + str(RoundCounter))

        #lets the player attack the next enemy after the previous one dies
        enemyCounter = enemies[i]
        player.displayStats()
        enemies[i].displayStats()

        #displays player move options
        playerOptions()
        #enemy does their attack
        #combat.enemyAttack(player, enemyCounter)
        if enemies[i].hp > 0:
            enemyOptions()

        #if the enemy dies then increment to the next one
        else:
            i+=1
            turnCounter = 0
            RoundCounter+=1
            #if i exceeds the amount of declared enemies then game over
            if i == len(enemies):
                print('You Win. Game over')
                break
            #if i does not exceed enemy amount then the next enemy appears
            else:
                player.awardCoins()
                displayShop()
                #displays the next enemy name after the previous one dies
                enemies[i].enemyIntro()
                #resets the players stats after an enemy dies
                player.resetStats()
        #if the players hp goes below 1 they die        
        if player.hp < 1:
            player.displayDeath()
        
        




   


