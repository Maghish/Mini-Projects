"""
The Pythonic Billing System
"""
# Hello
import csv
from tabulate import tabulate
import sys
from termcolor import colored
import json



class Admin():

    def __init__(self, file_name):
        self.file_name = file_name

    def search(self, item):
        if item.lower() == "all":
            all = []

            with open(self.file_name, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    all.append(row["item_name"])
            return [all, 2]
        else:
            Items = []

            with open(self.file_name, "r") as file:
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
        with open(self.file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['item_name'] == item:
                    return [False, 2]
                else:
                    pass

        with open(self.file_name, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["item_name", "item_price"])
            writer.writerow({"item_name": item.rstrip(), "item_price": price.rstrip()})
        return [True, 0]

class Customer():

    def __init__(self, file_name):
        self.file_name = file_name

    def search(self, item):
        if item.lower() == "all":
            all = []
            with open(self.file_name, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    all.append(row["item_name"])
            return [all, 2]
        else:
            Items = []
            with open(self.file_name, "r") as file:
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

class Keys():

        def get_data(self):
            with open("users.json") as f:
                users = json.load(f)
            return users

        def check_keys(self, keys):

            users = self.get_data()

            if keys in users:
                return True
            else:
                return False

        def create_keys(self, key, path):
            users = self.get_data()
            users[key] = {}
            users[key]["PATH"] = path
            with open("users.json", "w") as f:
                json.dump(users, f, indent= 1)
            return True

        def get_path(self, key):

            users = self.get_data()

            path = users[key]["PATH"]

            return path
        
        def get_all_keys(self):
            users = self.get_data()
            keys = []
            with open("users.json", "r") as f:
                users = json.load(f)
            for key in users:
                keys.append(key)
            return keys



def main():
    args = check_arg()
    if args == None:
        exit()
    elif args == False:
        setup_json()
        while True:
            interface = input(variables(3))
            if interface == '1' or interface.lower() == 'sign up':
                user = Keys()
                key = input("Key name: ")
                if key == 'exit':
                    exit("Shutdowning....")
                elif key == 'back':
                    pass
                else:
                    check = user.check_keys(key)
                    if check == True:
                        print(f"{key} already exists, try signing in")
                    else:
                        path = input("Path: ")
                        if not path.endswith(".csv"):
                            print("Not a csv file")
                        else:
                            user.create_keys(key, path)
                            file_name = path
                            file_name = setup_csv(file_name)
                            print(f"Successfully created {file_name} ✅")
                            while True:
                                mode = input(variables(1))

                                if mode == '1' or mode.lower() == "admin":
                                    admin(file_name)
                                elif mode == '2' or mode.lower() == "customer":
                                    customer(file_name)
                                elif mode == '3' or mode.lower() == "back":
                                    break
                                elif mode == '4' or mode.lower() == "exit":
                                    exit("Shutdowning.... ")
                                else:
                                    print("Invalid option")
                                    pass

            elif interface == '2' or interface.lower() == 'sign in':
                user = Keys()
                all_keys = user.get_all_keys()
                i = 0
                for keys in all_keys:
                    i += 1
                    print(f"{i}. {keys}")
                if i == 0:
                    print("There are no keys! Create a new key!")
                    continue
                else:
                    print(f"\n{i} keys found")
                    key = input("Key name: ")
                    if key == 'exit':
                        exit("Shutdowning....")
                    elif key == 'back':
                        pass
                    else:
                        check = user.check_keys(key)
                        if check == True:
                            path = user.get_path(key)
                            file_name = path
                            file_name = setup_csv(file_name)
                            print(f"Successfully connected with {file_name} ✅")
                            while True:
                                mode = input(variables(1))

                                if mode == '1' or mode.lower() == "admin":
                                    admin(file_name)
                                elif mode == '2' or mode.lower() == "customer":
                                    customer(file_name)
                                elif mode == '3' or mode.lower() == "back":
                                    break
                                elif mode == '4' or mode.lower() == "exit":
                                    exit("Shutdowning.... ")
                                else:
                                    print("Invalid option")
                                    pass

                        else:
                            print(f"There is no key called {key}, try creating a key")

            elif interface == '3' or interface.lower() == 'exit':
                exit("Shutdowning....")


            else:
                print("Invalid option")
                pass





def admin(file_name):
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
                        admin_item = Admin(file_name)
                        if price.strip().startswith("$"):
                            price = price.strip()
                        else:
                            price = f"${price.strip()}"
                        y = admin_item.add(name, price)
                        if y == [True, 0]:
                            print("Added ✅")
                            continue
                        elif y[0] == False and y[1] == 2:
                            print("Item already exists")
                            continue
                        elif y[0] == False and y[1] == 1:
                            print("Invalid input")
                    except:
                        print("Seems you missed comma ',' ?")
                        pass

            elif operation == '2' or operation.lower() == "search":
                while True:
                    item_name = input("Item name: ")
                    if item_name.lower() == "exit":
                        exit("Shutdowning.... ")
                    if item_name.lower() == "back":
                        break
                    admin_item = Admin(file_name)
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
                exit("Shutdowning....")








def customer(file_name):
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
            customer_item = Customer(file_name)
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

    return True

def variables(n):
    if n == 1:
        var = [['', "Modes"],
               [1, "Admin"],
               [2, "Customer"],
               [3, "Back"],
               [4, "Exit"]]
        var = f"\n{tabulate(var, headers='firstrow', tablefmt='fancy_grid')}\nSelect a option above: "
        return var
    elif n == 2:
        var = [['', 'Actions'],
               [1, 'Add items'],
               [2, 'Search'],
               [3, 'Back'],
               [4, 'Exit']]
        var = f"\n{tabulate(var, headers='firstrow', tablefmt='fancy_grid')}\nSelect a option above: "
        return var
    elif n == 3:
        var = [['', 'Keys'],
               [1, 'Create Key'],
               [2, 'Access Key'],
               [3, 'Exit']]
        var = f"\n{tabulate(var, headers='firstrow', tablefmt='fancy_grid')}\nSelect a option above: "
        return var

def check_arg(*args, **kwargs):
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "-kw":
            print(f"\n{colored('Special Keywords:', 'cyan')} {colored('back', 'yellow')}, {colored('exit', 'red')}, {colored('done' , 'green')}, {colored('all', 'blue')}\n")
            return True
        else:
            print("\nAvailable commands: -kw\n")
            return None

    else:
        return False


def setup_csv(path):
    try:
        with open(path, 'r') as f:
            return path
    except:
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(("item_name","item_price"))
            return path

def setup_json(filename = "users.json"):
    try:
        with open(filename) as f:
            return True
    except FileNotFoundError:
        with open(filename, 'w') as f:
            f.write('{}')
        return False















if __name__ == "__main__":
    main()