grocery_list=[]
Done=False
while not Done:
    
    ip= input("Do you want to add[A] or remove[R]: ")
    if ip=='A' or ip=='a':
        done= False
        while not done:
            item=input("Enter the item to be added: ")
            item.upper()
            grocery_list.append(item)
            op=input("Do you want to add again?[Y/N] ")
            if op=='Y' or op=='y':
                done= False
            else:
                done= True
        print(grocery_list)
    elif ip=='R' or ip=='r':
        done= False
        while not done:
            item=input("Enter the item to be removed: ")
            item.upper()
            grocery_list.remove(item)
            op=input("Do you want to remove again?[Y/N] ")
            if op=='Y' or op=='y':
                done= False
            else:
                done= True
        print(grocery_list)
    else:
        print("Wrong Input")
        print(grocery_list)
    io=input("Want to continue[Y/N]? ")
    if io=='Y' or 'y':
        Done=False
    else:
        Done=True
