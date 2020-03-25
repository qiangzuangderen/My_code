#coding=UTF-8

def dispalyInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory,addedItems):
    newdict = {}
    for i in addedItems:
        newdict.setdefault(i,1)
    newdict1 = {}
    newdict1.update(newdict)
    newdict1.update(inventory)
    return newdict1

inv = {'gold coin':42,'rope':1}
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
inv = addToInventory(inv,dragonLoot)
dispalyInventory(inv)


test = {}
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
for i in dragonLoot:
    test.setdefault(i,1)
print(test)


