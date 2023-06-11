import csv 

f = "" # You put your csv file's path or name 

class Admin():
    
    def search(self, item):
         Items = []
         with open(f, "r") as file:
             reader = csv.DictReader(file)
             for row in reader:
                 if row['item_name'] == item: 
                      price = row['item_price'].replace("$", "")
                      return [price, 1] 
                 elif row['item_name'].startswith(item) or item in row['item_name']: 
                      Items.append(row['item_name'])
                 else:
                     pass
         if len(Items) == 0:
            return False
         else:
            return [Items, 0]
             
    def add(self, item, price):
        with open(f, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['item_name'] == item: 
                    return False
                else:
                    pass
        with open(f, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["item_name", "item_price"])
            writer.writerow({"item_name": item.rstrip(), "item_price": price.rstrip()}) 

class Customer():

    def search(self, item):

        Items = []
        with open(f, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['item_name'] == item: 
                    price = row['item_price'].replace("$", "")
                    return [price, 1] 
                elif row['item_name'].startswith(item) or item in row['item_name']:
                    Items.append(row['item_name'])
                else:
                    pass
        if len(Items) == 0:
            return False
        else:
            return [Items, 0]




      
def main():
    while True:
        mode = input('''\n\nModes:
1. Admin
2. Customer
3. Exit 
Select a option above: ''')
        
        if mode == '1' or mode.lower() == "admin":
            admin()
        elif mode == '2' or mode.lower() == "customer":
            customer()

        elif mode == '3' or mode.lower() == "exit":
            exit("Shutdowning.... ")    
        else: 
            print("Invalid option")
            pass    



def admin():
    while True:
            operation = input('''\n\nActions:
1. Add items 
2. Search  
3. Back
4. Exit
Select a option above: ''')
            if operation == '1' or operation.lower() == "add items":
                while True:
                    result = input("Type as (Item_name, Item_price): ")
                    if result.lower() == "back":
                        break
                    if result.lower() == "exit":
                        exit()
                    try:
                        name, price = result.split(",")
                        admin_item = Admin()
                        if price.strip().startswith("$"):
                            price = price.strip()
                        else:
                            price = f"${price.strip()}"
                        admin_item.add(name, price)

                    except: 
                        print("Try again!")
                        pass
                
            elif operation == '2' or operation.lower() == "search":
                while True:
                    item_name = input("Item name: ")
                    if item_name.lower() == "exit":
                        exit("Shutdowning.... ")
                    if item_name.lower() == "back":
                        break
                    admin_item = Admin()
                    result = admin_item.search(item_name)
                    if result == False:
                        print("No Results found")
                        pass
                    elif result[1] == 0:
                        i = 0
                        for items in result[0]:
                            print(f"{i + 1}.{items}")
                            i += 1
                        print(f"{i} results found")
                    elif result[1] == 1:
                        print(f"Item: {item_name}\nPrice: ${result[0]}")    
            
            elif operation == '3' or operation.lower() == "back":
                break

            elif operation == '4' or operation.lower() == "exit":
                exit("Shutdowning.... ")
            
    




def customer():
    Items = 0
    while True:
        item = input("Item: ")
        if item.lower() == "exit":
            exit("Shutdowning.... ")
        if item.lower() == "back":
            break
        if item.lower() == "done":
            if Items == 0:
                exit("No items added\nThank You! Visit again!")
            else:
                exit(f"Total: ${Items}\nThank You! Visit again!")    
        customer_item = Customer()
        result = customer_item.search(item)

        if result == False:
            print("No Results found")
            pass
        else:
            if result[1] == 0:
                i = 0
                for items in result[0]:
                    print(f"{i + 1}.{items}")
                    i += 1
                print(f"{i} results found")
            elif result[1] == 1:
                print(f"Price: ${result[0]}")
                ask = input("Add to cart? Y/N ")
                if ask.lower() == "y":
                    print(f"{item} added to cart")
                    Items += int(result[0])
                    print(f"${Items}")
                elif ask.lower() == "n":
                    pass
                else:
                    print("Invalid Input")
                    pass 
            

        
if __name__ == "__main__":
    main()   
