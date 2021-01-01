count=int(input("enter the number of items: "))
item_lst=[]
for i in range (count):
    items=input("enter the item "+str(len(item_lst)+1)+":")
    item_lst.append(items)
    
def comma_code(lst):
    fnl_str=""
    for i in range (count):
        value=lst[i]
        if(i==count-1):
            fnl_str=fnl_str +"and " +lst[i]
            break
        else:
            fnl_str=fnl_str +value+", "
    print(fnl_str)
comma_code(item_lst)
