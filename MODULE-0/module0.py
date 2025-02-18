import os
import ast

inventory_data={}

def add():
    with open("./YIMinds/MODULE-0/data.txt", "r") as f:
        content = f.read()
    if not content:
        inventory_data = {}
    else:
        inventory_data = ast.literal_eval(content)
    prod_name = input("Enter the name of the product: ")
    price = float(input("Enter the price per product: "))
    quantity = int(input("Enter the quantity: "))
    total_price = price * quantity
    inventory_data[prod_name.upper()] = {
        'Price':price,
        'Quantity':quantity,
        'Total price':total_price
    }
    with open("./YIMinds/MODULE-0/data.txt","w") as f:
        f.write(str(inventory_data))
    print("Successfully added to the inventory data")

def update():
    with open("./YIMinds/MODULE-0/data.txt", "r") as f:
        inventory_data = ast.literal_eval(f.read())
    prod = input("Enter the product you want to update: ")
    if prod.upper() in inventory_data.keys():
        price = float(input("Enter the updated price per product: "))
        quantity = int(input("Enter the updated quantity: "))
        total_price = price * quantity
        inventory_data[prod.upper()] = {
        'Price':price,
        'Quantity':quantity,
        'Total price':total_price
        }
        with open("./YIMinds/MODULE-0/data.txt", "w") as f:
            f.write(str(inventory_data))
        print("Product is updated successfully")
    else:
        print("Product doesnt exist")

def view():
    with open("./YIMinds/MODULE-0/data.txt", "r") as f:
        prod_data = f.read()
        print(prod_data)

def search():
    with open("./YIMinds/MODULE-0/data.txt", "r") as f:
        inventory_data = ast.literal_eval(f.read())
    prod_name = input("Enter the name of the product you want to be searched: ")
    if prod_name.upper() in inventory_data.keys():
        print("The item is present")
    else:
        print("The item isnt present")

def main():
    while True:
        print("\nEnter choice:")
        print("1.Add")
        print("2.Update")
        print("3.View")
        print("4.Search")
        print("5.Exit")
        num = int(input())
        if num == 1:
            add()
        elif num == 2:
           update()
        elif num == 3:
            view()
        elif num == 4:
            search()
        elif num == 5:
            break
        else:
            print("Invalid number")
main()
