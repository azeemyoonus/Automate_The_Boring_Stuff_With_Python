stuff ={}
while True:
    print("Enter the item:")
    item=input()
    if item=="":
        break
    else:
        value=int(input("Enter the value: "))
    stuff[item]=value


def displayinventory(inventory):
    print("Inventory :")
    item_total=0
    for k, v in inventory.items():
        item_total += v
        print(v,end=" ")
        print(k)
        
       
    print("\nTotal number of items: "+str(item_total))

displayinventory(stuff)

def addToInventory(inventory,addedItems):
    for i in range(len(addedItems)):
        stuff.setdefault(addedItems[i],0)
        stuff[addedItems[i]]+=1
    return stuff


count=int(input("Enter the number of items to be added extra: "))
item_lst=[]
for i in range (count):
    items=input("Enter the item "+str(len(item_lst)+1)+":")
    item_lst.append(items)

inv=addToInventory(stuff,item_lst)
displayinventory(inv)
