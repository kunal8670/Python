#🔰 Challenge 1: Inventory Manager – Stock Alert System 💼 Scenario:

#You’re developing a simple inventory system for a shop.
#Each item has a name and quantity (e.g., ["Soap", 3], ["Toothpaste", 0]).
#You need to:
#Print all items that are out of stock.
#Alert the user if any item has quantity less than 2.


Stock=[["Soap",3],["Toothpast",0],["Chips",1]]

def AddQuantity(Stock): #to update Stock quantity
     tmp=0
     name=input("Enter name of Item: ")
     #quantity=int(input(f"Enter quantity of Item {name}:-"))

     for oname,oquantity in Stock:
          if oname==name:
            quantity=int(input(f"Enter quantity of Item {name}:-"))   
            oquantity+=quantity
            print(f"Now chips have {oquantity}")
          else:
            tmp+=1
     if tmp==len(Stock):
        print(f"Item name '{name}' not found in stock")      

def AddItem(Stock): #to add new item
    Item=input("Enter a name of 'Item':")
    quantity=int(input("Enter quantity:"))

    Stock.append([Item,quantity])
    print(Stock) #for test


def StockAlertSystem(Stock): #to chack stock alart
        for name,quantity in Stock:
            if(quantity==0):
                print(f"{name}: are out of stock")
            elif(quantity<2):
                 print(f"Alert {name}: have Onaly One Item\n")
            else:
                print("Dont have any alart")    


while True:    #man manu
    a=int(input("Enter 1: For Stock chack\nEnter 2: For update Stock\nEnter 3: Add new Item in Stock\n>"))
    if a==1:
        StockAlertSystem(Stock)
    elif a==2:
        AddQuantity(Stock)
    elif a==3:
        AddItem(Stock)
    elif a==0:
        print("Have a good day")
        break
        
         