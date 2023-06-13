# The Pythonic Billing System
#### Video Demo:  <URL HERE>
## Description: 
This is a simple billing system which is designed by Python language. You can add items, search items in `Admin` mode and in `Customers` mode, you can search for available products and if you gave the exact name of the product, it will ask you to whether add it to the cart of yours. At last you can type the keyword "**`done`**" to end the search and return you the total price of the products in the cart. **IMPORTANT NOTE:** It is a necessary to add `setup.py` to with the `index.py` file since the `setup.py` will make a clean csv file for the program to work with, and it is not recommended to create a csv file by yourself. So just do the following to setup the project:

1.  `setup.py` must be in the same directory of `index.py` 
2.  in the `index.py` you will find this line commented in the code and in that there will be a variable called **file_name** with empty double quotes, and in that type in any file that you want it to stored in and if the file is not created yet, don't worry that's what the `setup.py` is for. It will create or edit a csv file satisfy the requirements of the `index.py`.
```python
file_name = "" # File name/File path
file_name = setup(file_name)
``` 
3. If you done all the steps above, then you are good to go! Check out the Tutorial or the video demo for more information on how to use this program.
 
# Tutorial:
 ```md
Modes:
1. Admin
2. Customer
3. Exit 
Select a option above: 
```
so this is the first thing that the program will prompt. there are total two modes in this system, `Admin` and `Customer`. `Admin` allows you the administrator permissions like adding items in the respected csv file and search it's price. `Customer` is the actual mode for _billing_ stuff. You can search for items and add them to your cart and get the total amount of money you need to pay to buy the items in your cart. Throught the program there will be two keywords `exit` to exit the program and `back` to return back to the previous menu. there will be also one more keyword while in search action in customer mode, type `done` to finish shopping/billing and return back the total amount.
# 
# Admin
If you selected `Admin` mode, then this will be prompted:
```md
Actions:
1. Add items 
2. Search  
3. Back
4. Exit
Select a option above: 
```
#
# 
#### `Add items | 1`:
this action will let you to add your items of your choice and you would likely to be prompted as:
```md
Type as (Item_name, Item_price): 
```
In this you can type the items as `<Item_name>, <Item_price>`.   
example: 
```md
Type as (Item_name, Item_price): Ketchup, $20
```
Note that `,` is important in the input. With that the item will be added and the program will reprompt you again. If you are done adding the items you desired, then type the keyword `back` to get back to action menu or if you want to exit the program then type the keyword `exit` to exit the program.
#
#  
#### `Search | 2`:
this action let's you search for the item's price but it has a few features aswell:

```md
Item name: 
```
this is what the program will prompt, let's say there is a item called **Milk 100ml** and there is also a item called **Milk 500ml** where both of them are Milk but with different quantities. Well if input like
```md
Item name: Milk
```
then the program will prompt:
```md
Item name: Milk
1. Milk 100ml
2. Milk 500ml

2 results found
Item name: 
```
this resembles that there are two products in the name Milk, but you want to know the price of **Milk 500ml** _which is $20_, then type the extact name of the product to get the price of the respected product:
```md
Item name: Milk 500ml
Item: Milk 500ml
Price: $20
```
#
#
#### `Back | 3`:
This let's you get back to the actions menu again.
#
#
#### `Exit | 4`:
This will straight up exit the program.
#
# Customer
This straight away asks you a item to search for:
```md
Item:  
```
You can use the keyword `all` to find all the items available. Let's say you added _Ketchup_ for $40 and you are in customer mode and want to find the ketchup. You can just type:
```md
Item: all
```
then it will prompt the items which starts with "K" or what input you gave:
```md
Item: K
1. Kakarot Noodles
2. Ketchup  
```
then if you type the exact name of the product then it will prompt you to add to the cart:
```md
Item: Ketchup
Price: $40
Add to cart? Y/N
```
if you type "N" then it will reprompt again, but if you responded with "Y" then it will add the product to the cart and prompt the total price of the products in the cart so far:
```md
Item: Ketchup
Price: $40
Add to cart? Y/N y
Till now total: $40
Item: 
```
after shopping all the stuff you need, you can simply type in **`done`** to end the loop and bill all the stuff you have in your cart and return you the total amount of money you have to pay them.
```md
Item: done


Items    Price
------- -------
Ketchup  $40
------- -------
Total: $40


Thank you! Visit Again!
```
and That was the project! If you want to know about the keywords of the projects then type this in the command line to get the list of keywords:
```txt
$ python index.py -kw
```