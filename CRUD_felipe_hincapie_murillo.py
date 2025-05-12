#inventory software for a store "The hope"
import time #i use this  for simulate processing time

shop = {   #in future hope's store can have another modules like, workers, payments, so thats because i use this estructure. Also its looks like more lika a json file
    "inventory": [ #a list of dictionarys
        {
          "item_name": "cocacola", #string
          "item_amount" : 34,      #int
          "item_price" : 7500.0    #float
        },
        {
          "item_name": "battery", #string
          "item_amount" : 15,      #int
          "item_price" : 2500.0    #float 
        },
        {
          "item_name": "toilet paper", #string
          "item_amount" : 34,      #int
          "item_price" : 3500.0    #float 
        },
        {
          "item_name": "frozen_pizza", #string
          "item_amount" : 50,      #int
          "item_price" : 1500.0    #float 
        },
        {
          "item_name": "rice", #string
          "item_amount" : 150,      #int
          "item_price" : 4500.0    #float 
        }      

            ]  

     }

#Auxiliary functions 
# i don't want to repeat code so i made a function that calls another function

def ask_for_create():  #ask the user if want to create the item, if the answer is yes call the create_item() 
    ask_for_create = input(" 🤔🤔 Do you want to create it?  🤔🤔 (y/n)").lower().strip() #make a decision
    if ask_for_create == "y":
        
        print("The system will send you to the item creation module. 🫡🫡 ")
        time.sleep(1)
        create_item() #call a function  for create item
    else:
        print("exiting from search module")


def create_item(): #checked 
    item_inventory = shop["inventory"] #its like a bridge, helpme to connect with the content inside inventory, my items
    name_item = input("Enter the name of the item you want to add to inventory 🏷️🏷️  ").lower().strip() #methods to make the code more robust
    time.sleep(1) #non functionality but it's look more human friendly
    while True:# ensures that users enter an int
        try:
            item_amount = int(input('Enter the number of products you want to add to inventory. 📥📥   '))
            break
        except ValueError:
            print("Please enter a numeric value")
            continue
    time.sleep(1) #non functionality but it's look more human friendly
    while True: # ensures that users enter a float (number)
        try:
            item_price = float(input('enter the value of the product 💲💲  '))
            break
        except ValueError:
            print("Please enter a numeric value")
            continue

    item_creator = {
          "item_name": name_item , "item_amount" : item_amount , "item_price" : item_price} #groups all the information I want to add to the dictionary
    item_inventory.append(item_creator)#send dict to the list inventory
    time.sleep(1)
    print(f"{item_creator} Succesfully charged on system 🗃️🗃️  ")#confirmation


def check_products_in_inventory(): #checked
    name_item = input("Enter the name of the product you want to search for in the inventory: ➡️ ").lower().strip() #methods to make the code more robust
    item_inventory = shop["inventory"] #its like a bridge, helpme to connect with the content inside inventory, my items
    print("Processing  your query  🔍🔍🔍") #non functionality but it's look more human friendly
    time.sleep(1)
    
    for i in item_inventory: #search de name_item in the dictionary list
        if name_item == i["item_name"]:
            print("The item is in our inventory!!!")#confirms that the item exist
            time.sleep(1)
            print(f'▶️ Item name: {i["item_name"]}◀️ \n▶️ Item amount: {i["item_amount"]} ◀️\n▶️ Item price: {i["item_price"]}◀️  ') # print all the info
            return
    print(" 🚫 Sorry that item name doesn't exist 🚫")
    time.sleep(1)
    ask_for_create() #I think it makes my code more dinamic UX and UI are important to me, and i recycle code so its more efficient 


def update_item_price():
    name_item = input("Enter the name of the product whose price you want to update: ➡️ ").lower().strip()
    item_inventory = shop["inventory"]
    print("Processing  your query  🔍🔍🔍")
    time.sleep(1)
    
    for i in item_inventory:
        if name_item == i["item_name"]:  #in a future dev, the search module can be a function also, but right now i dont want to complicate myselft 
            print("Item found")
            time.sleep(1) 
            while True:
                while True:
                    try:
                        uptade_price = float(input(f"Enter the new price for {i["item_name"]}")) #ensures that te users enter a valid value
                        break
                    except ValueError:
                        print("The value isnt a number, please enter a number")
                if uptade_price <= 0:
                    print("🚫🚫looks like you enter a negative value, it cant be posible, try again🚫🚫") #A explicit feature asked for the test
                else:                
                    i["item_price"]= uptade_price
                    print("The item price was updated successfully ")#confirmation
                    print(f'▶️ Item name: {i["item_name"]}◀️ \n▶️ Item amount: {i["item_amount"]} ◀️\n▶️ Item price: {i["item_price"]}◀️  ')#resum of my code
                    return
    
    print(" 🚫 Sorry that item name doesn't exist 🚫")
    time.sleep(1)
    ask_for_create()

def delete_item_outstock(): 
    name_item = input("Enter the name of the product do you want delete from the inventory: ➡️ ").lower().strip()
    item_inventory = shop["inventory"]
    print("Processing  your query  🔍🔍🔍")
    time.sleep(1)
    
    for i in item_inventory:
        if name_item == i["item_name"]:
            print(f"Item {name_item} found")
            if i["item_amount"] == 0:
                print(f"the item: {i['item_name']} is ready to delete ")
                confirm_delete = input('Are you sure you want to delete the file? (y/n) \n⚠️⚠️This action is irreversible.⚠️⚠️ \n').lower().strip()#ensures that te users wants to erase a item
                if confirm_delete == 'y':
                    del item_inventory.remove[i]
                    print("the item was deleted succesfully")#confirm the action
                    return
                else:
                    print("Ok, the item wasnt deleted")
                    return
            else:
                print("🚫 You cannot delete the item because there are still products in the inventory.🚫")#A explicit feature asked for the test
                return
    
    print(" 🚫 Sorry that item name doesn't exist 🚫") #if the item doesnt exist, give the user the option to create it
    time.sleep(1)
    ask_for_create()

def price_of_all_inventary():#it was the more difficult part to me, lambda sucks hahah, actually its really helpfull but its more complicated
    item_inventory = shop["inventory"]

    if not item_inventory:
        print("the system is empty, cannot do the action")
        return
    total_value = sum(map(lambda item: item["item_price"] * item["item_amount"], item_inventory))
    print(f"💵💵💵 The total value of all inventory is {total_value:,.2f} 💵💵💵")#A explicit feature asked for the test
    return

        
def main(): #main function
    while True: 
        print("\n--- Hope's inventory sistem ---")
        print("1️⃣ Add item 📂 ")
        print("2️⃣ Consult item 🗂️")
        print("3️⃣ edit price of an item 💵")
        print("4️⃣ delete a product outstore 🚫")
        print("5️⃣ all price inventory 💰")
        print("6️⃣ exit 🔴🔴🔴") # Opción para terminar el programa

        opcion = input("Enter the number of the option you want to choose ").strip() # Leer la opción del usuario

        if opcion == "1":
            time.sleep(1)
            create_item()
        elif opcion == "2":
            time.sleep(1)
            check_products_in_inventory()
        elif opcion == "3":
            time.sleep(1)
            update_item_price()
        elif opcion == "4":
            time.sleep(1)
            delete_item_outstock()
        elif opcion == "5":
            time.sleep(1)
            price_of_all_inventary()
        elif opcion == "6":
            time.sleep(1)
            print("exiting program 😶‍🌫️😶‍🌫️ ")
            break 
        else:
            print("No valid option")

if __name__ == "__main__": #that ensures the program  runs locally and not as an import function
    main()
