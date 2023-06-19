from project import variables, setup_json, check_arg, Keys, Admin, Customer
from tabulate import tabulate



def test_vars():
    var = variables(1)
    var2 = [['', "Modes"],
               [1, "Admin"],
               [2, "Customer"],
               [3, "Back"],
               [4, "Exit"]]
    var2 = f"\n{tabulate(var2, headers='firstrow', tablefmt='fancy_grid')}\nSelect a option above: "
    assert str(var) == str(var2)

def test_setup_json():
    assert setup_json() == True

def test_args():
    assert check_arg("-kw") == None

def test_users():
    keys = Keys()
    assert keys.check_keys("Default") == False
    assert keys.create_keys("Default", "item.csv") == True 
    assert keys.check_keys("Default") == True


def test_admin():
    admin = Admin("items.csv")
    assert admin.search("all") ==  [[] , 2]
    assert admin.add("Bottle", "$10") == [True, 0]

def test_customer():
    customer = Customer("items.csv")
    assert customer.search("all") ==  [["Bottle"] , 2]
    

