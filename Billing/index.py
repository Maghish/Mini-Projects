import csv 
from tabulate import tabulate
import sys
from termcolor import colored
from setup import setup



file_name = "" # File name/File path
file_name = setup(file_name)


class Admin():
    
    def search(self, item):
        if item.lower() == "all":
            all = []
            with open(file_name, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    all.append(row["item_name"])
            return [all, 2]
        else:     
            Items = []
            with open(file_name, "r") as file:
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

        try:
            test_price = price.replace("$", "")
            test_price = int(test_price)
        except:
            return [False, 1]
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['item_name'] == item: 
                    return [False, 2]
                else:
                    pass
        
        with open(file_name, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["item_name", "item_price"])
            writer.writerow({"item_name": item.rstrip(), "item_price": price.rstrip()}) 

class Customer():

    def search(self, item):
        if item.lower() == "all":
            all = []
            with open(file_name, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    all.append(row["item_name"])
            return [all, 2]
        else:
            Items = []
            with open(file_name, "r") as file:
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
    check_arg()
    while True:
        mode = input(variables(1))
        
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
            operation = input(variables(2))
            if operation == '1' or operation.lower() == "add items":
                while True:
                    result = input("Item: ")
                    if result.lower() == "back":
                        break
                    if result.lower() == "exit":
                        exit("Shutdowning....")
                    try:
                        name, price = result.split(",")
                        admin_item = Admin()
                        if price.strip().startswith("$"):
                            price = price.strip()
                        else:
                            price = f"${price.strip()}"
                        y = admin_item.add(name, price)
                        if y == None:
                            print("Added ✅")
                            continue
                        elif y[0] == False and y[1] == 2:
                            print("Item already exists")
                            continue
                        elif y[0] == False and y[1] == 1:
                            print("Invaild input")
                    except: 
                        print("Seems you missed comma ','")
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
                            print(f"{i + 1}. {items}")
                            i += 1
                        print(f"\n{i} results found")
                    elif result[1] == 1:
                        print(f"Item: {item_name}\nPrice: ${result[0]}")    
                    elif result[1] == 2:
                        if len(result[0]) < 1:
                            print("No Results found")
                            continue
                        else:
                            i = 0
                            for thing in result[0]:
                                print(f"{i + 1}. {thing}")
                                i += 1
                            print(f"\n{i} results found")    
             
            elif operation == '3' or operation.lower() == "back":
                break

            elif operation == '4' or operation.lower() == "exit":
                exit("Shutdowning.... ")
            
    




def customer():
    S = []
    while True:
        item = input("Item: ")
        if item.lower() == "exit":
            exit("Shutdowning.... ")
        if item.lower() == "back":
            break


        if item.lower() == "done":
            data = []
            t = 0
            for thing in S:    
                    t = 0
                    for key in data:
                        if key['name'] == thing['item']:
                            key['amount'] += 1
                            t = 1
                            break
                        else:
                            pass    
                    if t == 0:
                        data.append({"name": thing['item'] , "value" : thing['price'], "amount": 1},)
                        continue
                    else:
                        pass
            final_data = [["Item", "Price", "Qty"]] 
            for thing in data:
                final_data.append([thing['name'], thing['value'], thing['amount']])     
                continue        
            print(f"\n\n{tabulate(final_data, headers= 'firstrow')}")
            amount = 0
            for s in S:
                amount += int(s['price'])
            print(f"----------------------------\nTotal: ${amount}")
            exit("\n\nThank you! Visit Again!\n\n")

        else:
            customer_item = Customer()
            result = customer_item.search(item)
            if result == False:
                print("No Results found")
                pass
            else:
                if result[1] == 0:
                    i = 0
                    for items in result[0]:
                        print(f"{i + 1}. {items}")
                        i += 1
                    print(f"\n{i} results found")
                elif result[1] == 1:
                    print(f"Price: ${result[0]}")
                    ask = input("Add to cart? Y/N ")
                    if ask.lower() == "y":
                        S.append({"item": item, "price": result[0]})
                        print(f"{item} added to cart")
                        amount = 0
                        for s in S:
                            amount += int(s['price'])
                        print(f"Till now total: ${amount}")
                    elif ask.lower() == "n":
                        pass
                    else:
                        print("Invalid Input")
                        pass 
                elif result[1] == 2:
                    if len(result[0]) < 1:
                        print("No Results found")
                        continue
                    else:
                        i = 0
                        for thing in result[0]:
                            print(f"{i + 1}. {thing}")
                            i += 1
                        print(f"\n{i} results found")        


def variables(n):
    if n == 1:
        var = [['', "Modes"],
               [1, "Admin"],
               [2, "Customer"],
               [3, "Exit"]]
        var = f"\n{tabulate(var, headers='firstrow', tablefmt='fancy_grid')}\nSelect a option above: "
        return var
    elif n == 2:
        var = [['', 'Actons'],
               [1, 'Add items'],
               [2, 'Search'],
               [3, 'Back'],
               [4, 'Exit']]
        var = f"\n{tabulate(var, headers='firstrow', tablefmt='fancy_grid')}\nSelect a option above: "
        return var     
    
def check_arg():
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "-admin" or sys.argv[1].lower() == "-a":
            admin()
        elif sys.argv[1].lower() == "customer" or sys.argv[1].lower() == "-c":
            customer()
        elif sys.argv[1].lower() == "-kw":
            print(f"\n{colored('Special Keywords:', 'cyan')} {colored('back', 'yellow')}, {colored('exit', 'red')}, {colored('done' , 'green')}{colored('(customer only)', 'black')}, {colored('all', 'blue')}{colored('(in search only)', 'black')}\n")
            exit()
        else:
            print("\nAvailable commands: -a, -c, -kw\n")
            exit()
        return
    else:
        return

        
if __name__ == "__main__":
    main()   