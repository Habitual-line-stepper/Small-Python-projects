# Import tabulate to create tables
# Import pycountry to check if the user enters an existing country
from tabulate import tabulate
from pycountry import pycountry


# Define the Shoes class
class Shoes:

    # Create the constructor and define methods for
    # country, code, product, cost, quantity
    # as well as the __str__ method to convert to a string
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def get_country(self):
        return self.country

    def get_code(self):
        return self.code

    def get_product(self):
        return self.product

    def update_quantity(self, updated_quantity):
        self.quantity = updated_quantity

    def __str__(self):
        return f"{self.country},{self.code}," \
               f"{self.product},{self.cost},{self.quantity}\n"


# Create two lists to hold the shoe objects
shoe_list = []
shoes_from_inventory = []


def read_shoes_data():
    # try to open the file inventory.txt as inventory
    try:
        with open("inventory.txt", "r") as inventory:
            # for each line in inventory
            for lines in inventory:
                # clean up the lines by stripping and splitting
                clean_up_lines = lines.strip("\n").split(",")
                # append to the shoes_from_inventory list
                shoes_from_inventory.append(clean_up_lines)
            # for each item in the list (from 1 to the end of the list)
            for item in range(1, len(shoes_from_inventory)):
                # Create a shoe variable to hold each item in the list
                shoe = shoes_from_inventory[item]
                # Create a shoe object using the Shoes class
                shoe_object = Shoes(shoe[0], shoe[1], shoe[2], shoe[3], int(shoe[4]))
                # append each object to the shoe_list list
                shoe_list.append(shoe_object)
    # if the file is not found
    except FileNotFoundError:
        # show the following error
        print("\nInvalid file. File does not exist.\n")


def user_country():
    # try to get input from the user
    while True:
        # ask the user to enter the country
        country = input("Please enter the country:\n")
        # check the country against the list of
        # countries in pycountry
        countries = str(list(pycountry.countries))
        # if the user enters a legitimate country
        if country in countries:
            # return country
            return country
        # else, print an error and continue looping
        else:
            print("Please enter a valid country!")


def user_cost():
    # try to get input from the user
    while True:
        try:
            # ask the user to enter the cost
            cost = int(input("Please enter the cost of the product:\n"))
            # return the cost
            return cost
        # if the user does not enter a number, print out the following error message
        except ValueError:
            print("\nPlease enter valid input!\n")


def user_quantity():
    # try to get input from the user
    while True:
        try:
            # ask the user to enter the quantity
            quantity = int(input("Please enter the quantity of the product:\n"))
            # return the quantity
            return quantity
        # if the user does not enter a number, print out the following error message
        except ValueError:
            print("\nPlease enter valid input!\n")


def capture_shoes():
    print("\n")
    # ask the user to enter the code of the product
    user_code = input("Please enter the code:\n")
    # ask the user to enter the name of the product
    user_product = input("Please enter the name of the product:\n")
    # create a new Shoes object, whilst calling the functions created above
    new_user_product = Shoes(user_country(), user_code,
                             user_product, user_cost(), user_quantity())
    # append the new Shoes object to the shoe_list list
    shoe_list.append(new_user_product)
    # open the inventory.txt file as a+ to append the new object
    with open("inventory.txt", "a+") as add_to_inventory:
        add_to_inventory.write(new_user_product.__str__())
        print("\nNew product successfully added!\n")


def view_all():
    print("\n")
    # create lists to hold the country, code, product, cost and quantity
    country_list = []
    code_list = []
    product_list = []
    cost_list = []
    quantity_list = []
    # for each item in shoe_list list
    # append the country, code, product, cost and quantity to
    # their respective lists
    for item in shoe_list:
        country_list.append(item.get_country())
        code_list.append(item.get_code())
        product_list.append(item.get_product())
        cost_list.append(item.get_cost())
        quantity_list.append(item.get_quantity())
    # use zip to create a new table_list variable holding all the above data
    table_list = zip(country_list, code_list,
                     product_list, cost_list, quantity_list)
    # use tabulate to print out the table_list list, with the format set to plain
    print(tabulate(table_list, headers=('Country', 'Code',
                                        'Product', 'Cost', 'Quantity'), tablefmt='plain'))
    print("\n")


def re_stock():
    print("\n")
    # create lists to hold the country, code, product, cost and quantity
    country_list = []
    code_list = []
    product_list = []
    cost_list = []
    quantity_list = []
    restock_list = []
    # sort the shoe list by quantity
    shoe_list.sort(key=lambda x: x.quantity)
    # for each item in shoe_list
    for item in range(1, len(shoe_list)):
        # append to the restock_list list
        restock_list.append(shoe_list[item])
    # for each item in restock_list
    for item in restock_list:
        # append the country, code, product, cost and quantity to
        # their respective lists
        country_list.append(item.get_country())
        code_list.append(item.get_code())
        product_list.append(item.get_product())
        cost_list.append(item.get_cost())
        quantity_list.append(item.get_quantity())

    # use zip to create a new table_list variable holding all the above data
    table_list = zip(country_list, code_list,
                     product_list, cost_list, quantity_list)
    # use tabulate to print out the table_list list, with the format set to plain
    # to show the quantities from smallest to largest
    # (from 1 to the length of the shoe_list list)
    print(tabulate(table_list, headers=('Country', 'Code', 'Product',
                                        'Cost', 'Quantity'), tablefmt='plain', showindex=range(1, len(shoe_list))))
    # while True, try to get integer input from the user
    while True:
        try:
            # ask the user which product they would like to restock
            select_item = int(input("\nPlease enter the number of the "
                                    "product you would like to restock:\n"))
            # ask them to enter the quantity they would like to restock
            restock_quantity = int(input("Please enter the new amount:\n"))
            # update the shoe_list list with the above value
            shoe_list[select_item].update_quantity(restock_quantity)
            # break out of the loop
            break
        # if there is a ValueError, print the following
        except ValueError:
            print("Please enter a valid number!")
    # Create an empty list to hold all items in shoe_list
    # as well as the newly updated item
    update_inventory = ""
    for item in shoe_list:
        update_inventory += \
            (f"{item.get_country()},{item.get_code()},{item.get_product()}"
             f",{item.get_cost()},{item.get_quantity()}\n")

    # Open up inventory.txt as w to write to it
    with open("inventory.txt", "w") as inventory:
        # write the new list to the text file
        inventory.write(update_inventory)
        # inform the user it was successful
        print("Restock successful!")
        print("\n")


def search_shoe():
    # Ask the user to enter the shoe code they are looking for
    user_search_for_shoe = input("Please enter the shoe code "
                                 "you are looking for:\n")
    # iterate through the shoe_list list
    for item in shoe_list:
        # if the entered shoe code matches a shoe code in the list
        if item.get_code() == user_search_for_shoe:
            # print out the shoe item
            print("The search has found the following:\n")
            print(f"{item}\n")


def value_per_item():
    print("\n")
    # create a variable to hold the total value
    total_value = 0
    # for each item in shoe_list list
    for item in shoe_list:
        # times item cost by item quantity
        item_value = int(item.get_cost()) * int(item.get_quantity())
        # add the total to total_value
        total_value += item_value
        # print out the value of each item and its code
        print(f"{item.get_code()}: R{item_value}")
    # print out the total value
    print(f"\nThe total value is: R{total_value}")
    print("\n")


def highest_qty():
    print("\n")
    # use max and lambda to get the item with the highest quantity
    # using the item.get_quantity method
    print(max(shoe_list, key=lambda item: item.get_quantity()))
    print("This shoe is now on sale, while stocks last!\n")


# initialize the read_shoes_data function
# so that the program reads all the data from the text file inventory.txt
# to the shoe_list list to be used throughout the program
read_shoes_data()
# Create a while loop for the "main menu"
while True:
    # try to get the user to enter a number that will
    # select one of the following options and will run the respective
    # function:
    try:
        user_select = int(input("Welcome! Please select from the following options:\n"
                                "1\t-\tCapture shoes\n"
                                "2\t-\tView all shoes\n"
                                "3\t-\tRestock shoes\n"
                                "4\t-\tSearch for shoes\n"
                                "5\t-\tView the value of the shoes\n"
                                "6\t-\tView which shoe has the highest quantity\n"))
        if user_select == 1:
            capture_shoes()
        elif user_select == 2:
            view_all()
        elif user_select == 3:
            re_stock()
        elif user_select == 4:
            search_shoe()
        elif user_select == 5:
            value_per_item()
        elif user_select == 6:
            highest_qty()
        else:
            # else tell the user to select a valid option
            print("Please enter a valid option!\n")
    # except if there is a value error,
    # ask the user to enter a valid number
    except ValueError:
        print("Please enter a valid number!\n")
