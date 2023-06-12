# The Pythonic Billing System
#### Video Demo:  <URL HERE>
## Description: 
This is a simple billing system which is designed by Python language. You can add items, search items in `Admin` mode and in `Customers` mode, you can search for available products and if you gave the exact name of the product, it will ask you to whether add it to the cart of yours. At last you can type the keyword "**`done`**" to end the search and return you the total price of the products in the cart.
### Tutorial:
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
Under development!



