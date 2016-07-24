# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
        # FILL IN THE CODE HERE
        item_total = item_total + value
        print (value,key)
        
        
        
        
        
        
    print("Total number of items: " + str(item_total))

displayInventory(stuff)


#
#Inventory:
#12 arrow
#42 gold coin
#1 rope
#6 torch
#1 dagger
#Total number of items: 62
