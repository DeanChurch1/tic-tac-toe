#Hero's inventory
import random
player_health = 100
player_armor = 1250
player_attack = 250
player_money = 0

inventory = ["rusty sword","leather armor","wood shield","small healing potion"]
player_stats = ["health",player_health,"armor",player_armor,
                "attack",player_attack,"money",player_money]
print("player stats")
print(player_stats)
print("Your items:")
for item in inventory:
    print(item)
input("\nPress the enter key to continue")
print("You have",len(inventory), "items in your possession.")

player_health -= 22
input("\nyou have taken some damage on your journey \n" +
      "your health is at " +str(player_health)+"\n"+
      "you need to use your healing potion \n Press the enter key to continue")

if "small healing potion" in inventory:
    print("You will live to fight another day by using the healing potion")
    player_health += 20
    print(player_stats)
    inventory.remove("small healing potion")
    for item in inventory:
        print(item)
        
index = int(input("\nEnter the index number for an item in inventory: "))
while index >len(inventory)-1 or index <0:
    print("that number is out of range")
    index = int(input("\nEnter the index number for an item in inventory: "))
print("At index",index,"is",inventory[index])

start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("enter the index number to end the slice: "))
print("inventory[",start, ":",finish,"] is", end="")
print(inventory[start:finish])

input("\nPress the enter key to continue.")

chest_items = ["gold","gems","elven sword","bow","corssbow","boots","hat"]
chest = []
for i in range(3):
    item = random.choice(chest_items)
    chest.append(item)
print("you find a chest which contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory now:")
print(inventory)

input("\nPress the neter key to continue.")
print("You trade your sword for a crossbow.")
inventory[0] = "crossbow"
print("your inventory is now:")
print(inventory)

input("\n Press the enter key to continue.")
print("You use your gold and gems to buy an orb of future telling.")
inventory[4:6] = ["orb of future telling"]
print("Inventory now",inventory)
input("\n Press teh neter key to continue.")
print("in a great battle, your shield is destroyed")
del inventory[2]
print("Your inventory is now:")
print(inventory)

print("Your crossbow and armor are stolen by thieves.")
del inventory[:2]
print("Your inventory is now:")
print(inventory)
